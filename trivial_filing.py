# This challenge is WIP
from support import hackattic
import threading
import tempfile
import tftpy
import os

IP = '0.0.0.0'
PORT = 18080


def request_validation(server_is_running, problem):
    server_is_running.wait()

    solution = {
        'tftp_host': hackattic.env.str('PUBLIC_IP'),
        'tftp_port': PORT,
    }

    print(problem.solve(solution))


def run():
    problem = hackattic.Problem('trivial_filing')

    data = problem.fetch()

    files = data['files']

    tmdir = tempfile.TemporaryDirectory()

    for filename, filecontent in files.items():
        with open(os.path.join(tmdir.name, filename), 'w') as f:
            f.write(filecontent)

    server = tftpy.TftpServer(tmdir.name)

    try:
        threading.Thread(target=request_validation, args=(server.is_running, problem), daemon=True).start()

        server.listen(IP, PORT)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
