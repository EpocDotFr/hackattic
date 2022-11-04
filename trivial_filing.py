from support import hackattic
import threading
import tempfile
import tftpy
import os

IP = '0.0.0.0'
PORT = 18080


def run():
    problem = hackattic.Problem('trivial_filing')

    data = problem.fetch()

    files = data['files']

    tmdir = tempfile.TemporaryDirectory()

    for filename, filecontent in files.items():
        with open(os.path.join(tmdir.name, filename), 'w') as f:
            f.write(filecontent)

    print(tmdir.name)

    server = tftpy.TftpServer(tmdir.name)

    try:
        threading.Thread(target=server.listen, args=(IP, PORT), daemon=True).start()

        solution = {
            'tftp_host': hackattic.env.str('PUBLIC_IP'),
            'tftp_port': PORT,
        }

        print(problem.solve(solution))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
