from support import hackattic
import sh

problem = hackattic.Problem('hosting_git')

data = problem.fetch()

push_token = data['push_token']
username = data['username']
repo_path = data['repo_path']
ssh_key = data['ssh_key']

with sh.contrib.sudo:
    sh.adduser(username, system=True, shell='/usr/bin/git-shell', group=True, disabled_password=True)

    home_dir = f'/home/{username}'
    ssh_dir = f'{home_dir}/.ssh'

    sh.mkdir(ssh_dir)
    sh.chown(f'{username}:{username}', ssh_dir)
    sh.chmod('700', ssh_dir)

    authorized_keys_file = f'{ssh_dir}/authorized_keys'

    sh.touch(authorized_keys_file)
    sh.chown(f'{username}:{username}', authorized_keys_file)
    sh.chmod('600', authorized_keys_file)

    sh.tee(sh.echo(f'no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty {ssh_key}'), authorized_keys_file, a=True)

    repo_path = f'{home_dir}/{repo_path}'

    sh.git.init(repo_path, bare=True)
    sh.chown(f'{username}:{username}', repo_path, R=True)

response = hackattic.requests.post(f'https://hackattic.com/_/git/{push_token}', json={'repo_host': hackattic.env.str('PUBLIC_IP')})
response.raise_for_status()

with open(f'{repo_path}/solution.txt', 'r') as f:
    solution = {
        'secret': f.read()
    }

print(problem.solve(solution))
