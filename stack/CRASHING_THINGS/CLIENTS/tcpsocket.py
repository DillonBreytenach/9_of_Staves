import socket
#from socket import *
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print(str(e))
    sys.exit()
    
print("SOCKET CREATED")

target_host="127.0.0.1"
target_port=80

try:
    s.connect((target_host, int(target_port)))
    print("[SOCKET]::[CONNECTED]", target_host, str(target_port))
    s.shutdown(2)
except Exception as e:
    print(e)
    sys.exit()
    