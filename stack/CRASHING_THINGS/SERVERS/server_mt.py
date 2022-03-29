#V 0.1

import socket
from _thread import *

s = socket.socket()

host="127.0.0.1"
port=5252
Thread_count = 0

try:
    s.bind(('', port))
except Exception as e:
    print(e)

print("[WAITING FOR CLIENTS]:  ")    
s.listen(5)

def client_thread(connection):
    connection.send(str.encode("[INIT][SERVER]"))
    while True:
        data = connection.recv(1024 * 2)
        reply = "[SERVER] "+data.decode("utf-8")
        if not data:
            break
        else:
            print("[CLIENT]: ", str(reply))
        connection.sendall(str.encode(reply))
    connection.close()
    
    
while True:
    client, addr = s.accept()
    print("[CONNECTED] : ", client, addr[0], str(addr[1]))
    start_new_thread(client_thread, (client,))
    Thread_count+=1
    print("[THREAD_COUNT] : ", str(Thread_count))

s.close()    
