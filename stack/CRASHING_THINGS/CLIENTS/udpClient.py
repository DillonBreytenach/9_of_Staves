import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


msg = "[FROM::CLIENT]"
client_sock.sendto(msg.encode(),('127.0.0.1', 80))
data, addr = client_sock.recvfrom(1024*3)
print('[SERVER]:: ', str(data))
client_sock.close()