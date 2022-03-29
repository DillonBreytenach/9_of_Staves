from multiprocessing import connection
import socket
from _thread import *

S_sock = socket.socket()

host= "127.0.0.1"
port=80

Thread_Count = 0
try:
    S_sock.bind(host, port)
except Exception as e:
    print(e)

S_sock.listen(5)

print("WAITING FOR CONNECTION: ")

def client_thread(conn):
    conn.send(str.encode("WELCOME"))
    while True:
        data = conn.recv(1024*2)
        re = "IM SERVER : "+ data.decode()
        if not data:
            break
        conn.sendall(str.encode(re))
    conn.close()
    
    
while True:
    client, addr = S_sock.accept()
    print("[CONNECTED] : ", addr[0], str(addr[1]))
    start_new_thread(client_thread, (client,))
    Thread_Count += 1
    print("[THREAD_COUNT]: ", str(Thread_Count))
    
S_sock.close()
