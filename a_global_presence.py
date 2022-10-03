from support import hackattic, requests


problem = hackattic.Problem('a_global_presence')

data = problem.fetch()

presence_token = data['presence_token']

# Good luck finding 7 working proxies
proxies = [
    '101.109.176.134:8080',
    '101.109.176.134:8080',
    '101.109.176.134:8080',
    '101.109.176.134:8080',
    '101.109.176.134:8080',
    '101.109.176.134:8080',
    '101.109.176.134:8080',
]

for proxy in proxies:
    print(proxy)

    response = requests.get(f'https://hackattic.com/_/presence/{presence_token}', proxies={'https': proxy})
    response.raise_for_status()

print(problem.solve({}))
