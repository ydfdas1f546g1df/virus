import socket
import threading
import time

HOST = '192.168.101.114'
PORT = 8585


def connection(connect):
    print(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    threads = []
    while True:
        conn, addr = s.accept()
        with conn:
            x = threading.Thread(target=connection(conn), daemon=True)
            x.start()
            threads.append(x)

        
