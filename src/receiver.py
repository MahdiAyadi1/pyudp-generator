import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5000))

while True:
    data, addr = sock.recvfrom(65535)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Received {len(data)} bytes from {addr}")