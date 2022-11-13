# This challenge is WIP
# This script requires PORT to be forwarded for TCP trafic on your router to the machine running this script
from dnslib.zoneresolver import ZoneResolver
from dnslib.server import DNSServer
from support import hackattic

IP = '0.0.0.0'
PORT = 18080


def run():
    problem = hackattic.Problem('serving_dns')

    data = problem.fetch()

    records_raw = data['records']
    records_by_type = {
        record['type']: record for record in records_raw
    }

    zone = []

    for type_, record in records_by_type.items():
        name = record['name']
        data = record['data']

        if type_ == 'TXT':
            data = f'"{data}"'
        elif type_ == 'RP':
            for sub_record in [record_raw for record_raw in records_raw if record_raw['type'] in ('A', 'AAAA')]:
                sub_type = sub_record['type']
                sub_data = sub_record['data']

                zone.append(f'{data}. 60 IN {sub_type} {sub_data}')

            data = f'{data}. .'

        zone.append(f'{name}. 60 IN {type_} {data}')

    print(zone)

    server = DNSServer(ZoneResolver('\n'.join(zone)), IP, PORT)

    try:
        server.start_thread()

        solution = {
            'dns_ip': hackattic.env.str('PUBLIC_IP'),
            'dns_port': PORT,
        }

        print(problem.solve(solution))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
