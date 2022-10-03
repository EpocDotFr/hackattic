from twisted.internet import reactor, ssl
from autobahn.twisted import websocket
from support import hackattic
import time


class WebsocketChitChatClientProtocol(websocket.WebSocketClientProtocol):
    def onOpen(self):
        super(WebsocketChitChatClientProtocol, self).onOpen()

        self.last_ping = self.now_as_ms()

    def onMessage(self, payload, isBinary):
        if isBinary:
            raise NotImplementedError()

        payload = payload.decode('utf8')

        print(payload)

        if payload == 'ping!':
            now = self.now_as_ms()
            diff = now - self.last_ping

            print(diff, end='')

            interval = 0

            if 500 <= diff <= 900:
                interval = 700
            elif 1300 <= diff <= 1700:
                interval = 1500
            elif 1800 <= diff <= 2200:
                interval = 2000
            elif 2300 <= diff <= 2700:
                interval = 2500
            elif 2800 <= diff <= 3200:
                interval = 3000

            print(f' > {interval}')

            self.sendMessage(str(interval).encode('utf8'))

            self.last_ping = now
        elif payload.startswith('congratulations'):
            solution = {
                'secret': payload.replace('congratulations! the solution to this challenge is ', '').strip('"')
            }

            print(problem.solve(solution))

    def now_as_ms(self):
        return int(time.time() * 1000)


problem = hackattic.Problem('websocket_chit_chat')

data = problem.fetch()

token = data['token']

factory = websocket.WebSocketClientFactory(f'wss://hackattic.com/_/ws/{token}')
factory.protocol = WebsocketChitChatClientProtocol

websocket.connectWS(factory, ssl.ClientContextFactory())

reactor.run()