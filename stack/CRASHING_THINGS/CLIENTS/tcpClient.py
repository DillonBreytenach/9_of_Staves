import socket
import sys

payload = '[CLIENT] >> [SERVER]'


try:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print(str(e))
    sys.exit()
    
try:
    client_sock.connect(('127.0.0.1', 80))
except Exception as e:
    print(e)
    sys.exit()
    
try:
    while True:
        client_sock.send(payload.encode('utf-8'))
        data = client_sock.recv(1024*2)
        print(str(data))
        more=input("[CLIENT]>[SERVER]: ")
        if more.lower() == 'y':
            payload=input("PAYLOAD: ")
        else:
            print("CLOSED BY USER")
            
except KeyboardInterrupt:
    print("[USER]: EXITED")
    
client_sock.close()

