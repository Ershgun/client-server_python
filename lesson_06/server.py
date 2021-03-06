 
"""Программа-сервер"""
import json
import logging
from socket import AF_INET, SOCK_STREAM, socket
from lesson_06.utils.utils import create_parser
from lesson_06.utils.variables import ENCODING, MAX_CONNECTIONS, MAX_PACKAGE_LENGTH
from lesson_06.utils.decorators import log_de

import lesson_06.log.server_log_config

RESPONSE_ERROR = 400
RESPONSE_OK = 200

SERVER_LOGGER = logging.getLogger('server')


class Server:
    def __init__(self, logger):
        self.logger = logger
        self.transport = socket(AF_INET, SOCK_STREAM)
        self.addr, self.port = create_parser()
        self.logger.info(f'Сервер создан с параметрами {self.addr} {self.port}')

    @log_de
    def create_connection(self):
        try:
            self.transport.bind((self.addr, self.port))
            self.transport.listen(MAX_CONNECTIONS)
        except Exception as e:
            self.logger.critical(f'Сервер не подключен {e}')

        while True:
            client, client_address = self.transport.accept()
            response = RESPONSE_ERROR
            try:
                data = client.recv(MAX_PACKAGE_LENGTH)
                if data:
                    json_answer = data.decode(ENCODING)
                    response = self.process_client_message(json.loads(json_answer))
            except:
                self.logger.error(f'Принято некорректное сообщение от клиента')
            finally:
                self.logger.info(f'Отвечаем клиенту {response}')
                print(f'Отвечаем клиенту', response)
                client.send(f'{response}'.encode(ENCODING))
                client.close()

    @log_de
    def process_client_message(self, message):
        self.logger.info(f'Обработка сообщения {message}')
        print('process_client_message', message)
        if message['action'] == 'presence' and message['user']['account_name'] == 'GUEST':
            return RESPONSE_OK
        return RESPONSE_ERROR


def main():
    server = Server(SERVER_LOGGER)
    server.create_connection()


if __name__ == '__main__':
    main()
