# This script requires:
#   - extra Python packages: pip install pyjwt
from http import HTTPStatus
import urllib.parse
import http.server
import hackattic
import jwt
import io

BIND_IP = '0.0.0.0'
PUBLIC_IP = ''
PORT = 8080


class JottingJwtsServer(http.server.ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True


class JottingJwtsHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)

        if parsed_path.path != '/':
            self.send_error(HTTPStatus.NOT_FOUND)

            return

        self.send_response(200)

        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write('Hello'.encode('utf-8'))

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


def run_http_server():
    with JottingJwtsServer((BIND_IP, PORT), JottingJwtsHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

problem = hackattic.Problem('jotting_jwts')

data = problem.fetch()

jwt_secret = data['jwt_secret']

solution = {
    'app_url': f'http://{PUBLIC_IP}:{PORT}/'
}

print(problem.solve(solution))

run_http_server()
