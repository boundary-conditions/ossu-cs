

import socket

ADDR, PORT = 'data.pr4e.org', 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
    mysock.connect((ADDR, PORT))
    cmd = b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'
    mysock.send(cmd)

    content_length = None
    while content_length is None or content_length > 0:
        data = mysock.recv(512).decode()
        if content_length is None:
            head, data = data.split('\r\n\r\n')
            for line in head.splitlines():
                if line.lower().startswith('content-length'):
                    content_length = int(line.split()[-1])
                    break
        content_length -= len(data)
        print(data, end='')