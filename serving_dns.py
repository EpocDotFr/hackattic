# This challenge is WIP
# This script requires PORT to be forwarded for TCP trafic on your router to the machine running this script
from dnslib.zoneresolver import ZoneResolver
from dnslib.server import DNSServer
from support import hackattic
import io

IP = '0.0.0.0'
PORT = 18080


def run():
    problem = hackattic.Problem('serving_dns')

    data = problem.fetch()

    records = data['records']

    zone = ''

    for record in records:
        name = record['name']
        type_ = record['type']
        data = record['data']

        if type_ == 'TXT':
            data = f'"{data}"'
        elif type_ == 'RP':
            data = f'{data}. .'

        zone += f'{name}. 60 IN {type_} {data}\n'

    print(zone)

    server = DNSServer(ZoneResolver(zone), IP, PORT)

    try:
        server.start_thread()

        solution = {
            'dns_ip': hackattic.env.str('PUBLIC_IP'),
            'dns_port': PORT,
        }

        # print(problem.solve(solution))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
