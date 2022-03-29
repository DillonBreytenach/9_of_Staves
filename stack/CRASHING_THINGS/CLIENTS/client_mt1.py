#V 0.1
import socket

c = socket.socket()

host= "127.0.0.1"
port= 5252

print("{ATTEMPING} : [CONNECTION]")
try:
    c.connect((host,port))
except socket.error as e:
    print(str(e))
    

resp = c.recv(1024*2)
print("RE:: "+ resp.decode())
while True:
    In_Com = input("> ")
    c.send(str.encode(In_Com))
    resp = c.recv(1024*2)
    print("RE: "+ resp.decode())
    
c.close()