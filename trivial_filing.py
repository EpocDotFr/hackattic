from ptftplib import tftpserver
from support import hackattic
import threading
import tempfile
import os

IFACE = 'wlp0s20f3'
PORT = 18080


class TrivialFillingTFTPServer(tftpserver.TFTPServer):
    def __init__(self, *args, **kvargs):
        super(TrivialFillingTFTPServer, self).__init__(*args, **kvargs)

        self.ready_event = threading.Event()

    def serve_forever(self):
        self.ready_event.set()

        super(TrivialFillingTFTPServer, self).serve_forever()


def run():
    problem = hackattic.Problem('trivial_filing')

    data = problem.fetch()

    files = data['files']

    tmdir = tempfile.TemporaryDirectory()

    for filename, filecontent in files.items():
        with open(os.path.join(tmdir.name, filename), 'w') as f:
            f.write(filecontent)

    server = TrivialFillingTFTPServer(IFACE, tmdir.name, PORT)

    try:
        threading.Thread(target=server.serve_forever, daemon=True).start()

        server.ready_event.wait()

        solution = {
            'tftp_host': hackattic.env.str('PUBLIC_IP'),
            'tftp_port': PORT,
        }

        print(problem.solve(solution))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
