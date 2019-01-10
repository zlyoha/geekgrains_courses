"""
Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
  клиент отправляет запрос серверу;
  сервер отвечает соответствующим кодом результата.

Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.

Функции клиента:
  сформировать presence-сообщение;
  отправить сообщение серверу;
  получить ответ сервера;
  разобрать сообщение сервера;
  параметры командной строки скрипта client.py <addr> [<port>]:

addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.

Функции сервера:
  принимает сообщение клиента;
  формирует ответ клиенту;
  отправляет ответ клиенту;
  имеет параметры командной строки:

-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

“action”: “presence” — присутствие. Сервисное сообщение для извещения сервера о присутствии клиента online;
“action”: “prоbe” — проверка присутствия. Сервисное сообщение от сервера для проверки присутствии клиента online;
“action”: “msg” — простое сообщение пользователю или в чат;
“action”: “quit” — отключение от сервера;
“action”: “authenticate” — авторизация на сервере;
“action”: “join” — присоединиться к чату;
“action”: “leave” — покинуть чат.

"""


def get_from_client():
    pass


def prepare_response():
    pass


def send_to_client():
    pass


# -p port, default 7777
# -a addr
def main():
    pass


if __name__ == '__name__':
    main()
