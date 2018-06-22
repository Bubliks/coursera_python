import socket
import time

from collections import defaultdict


class ClientError(Exception):
    pass


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.buf_size = 1024
        self.sock = socket.create_connection((self.ip, self.port), self.timeout)

    def put(self, metric_name, value, timestamp=None):
        timestamp = str(int(time.time())) if timestamp is None else str(timestamp)
        packet = ' '.join(['put', metric_name, str(float(value)), timestamp + '\n'])

        self.sock.sendall(packet.encode('utf-8'))
        err = self.sock.recv(self.buf_size).decode()

        if err == 'error\nwrong command\n\n':
            raise ClientError()

    @staticmethod
    def _data_parser(data):
        tmp = data.lstrip('ok\n').rstrip('\n\n')
        return [line.split() for line in tmp.split('\n')]

    def get(self, metric_name):
        packet = 'get {}\n'.format(metric_name)

        self.sock.sendall(packet.encode('utf-8'))
        err = self.sock.recv(self.buf_size).decode()

        if err == 'ok\n\n':
            return {}
        if err == 'error\nwrong command\n\n':
            raise ClientError()

        data = self._data_parser(err)
        result = defaultdict(list)
        for key, metric, timestamp in data:
            result[key].append((int(timestamp), float(metric)))

        return result


def main():
    client = Client('127.0.0.1', 8888)
    client.put('kekes', 1244, 888)
    client.put('kekes', 12, 3)
    client.put('kek', 124, 91)
    client.get('*')


if __name__ == '__main__':
    main()