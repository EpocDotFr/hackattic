# This script requires PORT to be forwarded for TCP trafic on your router to the machine running this script
from support import hackattic
from http import HTTPStatus
import urllib.parse
import http.server
import threading
import json
import jwt

IP = '0.0.0.0'
PORT = 18080


class JottingJwtsServer(http.server.ThreadingHTTPServer):
    allow_reuse_address = True

    def __init__(self, *args, jwt_secret=None, **kvargs):
        super(JottingJwtsServer, self).__init__(*args, **kvargs)

        self.jwt_secret = jwt_secret
        self.append = ''
        self.ready_event = threading.Event()

    def service_actions(self):
        self.ready_event.set()


class JottingJwtsHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)

        if parsed_path.path != '/':
            self.send_error(HTTPStatus.NOT_FOUND)

            return
        elif 'content-length' not in self.headers:
            self.send_error(HTTPStatus.LENGTH_REQUIRED)

            return

        content_length = int(self.headers.get('content-length'))

        encoded_jwt = self.rfile.read(content_length)

        try:
            decoded_jwt = jwt.decode(encoded_jwt, self.server.jwt_secret, algorithms='HS256')
        except:
            self.send_error(HTTPStatus.BAD_REQUEST)

            return

        if 'append' in decoded_jwt:
            self.server.append += decoded_jwt['append']

            self.send_error(HTTPStatus.NO_CONTENT)
        else:
            self.send_response(200)

            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            self.wfile.write(json.dumps({
                'solution': self.server.append
            }).encode('utf-8'))

    def do_GET(self):
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    def do_PUT(self):
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    def do_PATCH(self):
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    def do_DELETE(self):
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    def do_OPTIONS(self):
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    def do_HEAD(self):
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)


problem = hackattic.Problem('jotting_jwts')

data = problem.fetch()

with JottingJwtsServer((IP, PORT), JottingJwtsHandler, jwt_secret=data['jwt_secret']) as server:
    try:
        threading.Thread(target=server.serve_forever, daemon=True).start()

        server.ready_event.wait()

        solution = {
            'app_url': 'http://{}:{}/'.format(hackattic.env.str('PUBLIC_IP'), PORT)
        }

        print(problem.solve(solution))
    except KeyboardInterrupt:
        pass
