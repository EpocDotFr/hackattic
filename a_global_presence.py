from support import hackattic, requests


problem = hackattic.Problem('a_global_presence')

data = problem.fetch()

presence_token = data['presence_token']

proxies = [
    ('91.137.33.106', 8080),
    ('23.82.16.149', 3128),
    ('64.235.204.107', 3128),
    ('157.100.12.138', 999),
    ('173.212.200.30', 3128),
    ('194.5.193.73', 8080),
    ('92.43.120.95', 3128),
]

for proxy in proxies:
    print(proxy)

    ip, port = proxy

    response = requests.get(f'https://hackattic.com/_/presence/{presence_token}', proxies={'https': f'{ip}:{port}'})
    response.raise_for_status()

print(problem.solve({}))
