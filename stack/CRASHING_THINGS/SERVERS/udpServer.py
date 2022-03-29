import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 80))
#server_socket.listen(5)


while True:
    data, addr = server_socket.recvfrom(1024 *3)
    print("[CLIENT]: ", str(data))
    msg = "[SERVER::]"
    msg = bytes(msg.encode())
    server_socket.sendto(msg, addr)
    