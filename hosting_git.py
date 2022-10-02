# Ths script requires the current user to be sudoer (https://amoffat.github.io/sh/sections/sudo.html#etc-sudoers-nopasswd)
from support import hackattic
import sh

problem = hackattic.Problem('hosting_git')

data = problem.fetch()

push_token = data['push_token']
username = data['username']
repo_path = data['repo_path']
ssh_key = data['ssh_key']

home_dir = f'/home/{username}'
ssh_dir = f'{home_dir}/.ssh'
authorized_keys_file = f'{ssh_dir}/authorized_keys'
repo_path = f'{home_dir}/{repo_path}'

with sh.sudo:
    sh.adduser(username, system=True, shell='/usr/bin/git-shell', group=True, disabled_password=True)

with sh.sudo(u=username, _with=True):
    sh.mkdir(ssh_dir)
    sh.chown(f'{username}:{username}', ssh_dir)
    sh.chmod('700', ssh_dir)
    sh.touch(authorized_keys_file)
    sh.chown(f'{username}:{username}', authorized_keys_file)
    sh.chmod('600', authorized_keys_file)

    sh.tee(sh.echo(f'no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty {ssh_key}'), authorized_keys_file, a=True)

    sh.contrib.git.init(repo_path, bare=True)
    sh.chown(f'{username}:{username}', repo_path, R=True)

    sh.cd(repo_path)

    response = hackattic.requests.post(f'https://hackattic.com/_/git/{push_token}', json={'repo_host': hackattic.env.str('PUBLIC_IP')})
    response.raise_for_status()

    solution = {
        'secret': sh.contrib.git.show('master:solution.txt').stdout.decode()
    }

    print(problem.solve(solution))
