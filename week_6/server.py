import asyncio

from collections import defaultdict


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    data_storage = defaultdict(list)

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode('utf-8'))

    def process_data(self, data):
        data_arr = data.split()
        if data_arr[0] == 'put':
            self.put(data_arr[1:])
            return 'ok\n\n'
        elif data_arr[0] == 'get':
            return 'ok\n' + self.get(data_arr[1]) + '\n'
        else:
            return 'error\nwrong command\n\n'

    def get(self, key_data):
        res = ''
        if key_data == '*':
            for key in ClientServerProtocol.data_storage.keys():
                for item in ClientServerProtocol.data_storage[key]:
                    res += key + ' {} {}\n'.format(item[0], item[1])
            print(res)
        else:
            for item in ClientServerProtocol.data_storage[key_data]:
                res += key_data + ' {} {}\n'.format(item[0], item[1])
        return res

    def put(self, data):
        ClientServerProtocol.data_storage[data[0]].append((data[1], data[2]))

#run_server('127.0.0.1', 8888)