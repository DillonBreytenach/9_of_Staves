#CONNECTION__
import socket
import threading


#CONNECTION CLASSES
class connections():
    def __init__(self, **kwargs):
        self.val = ""
       
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8084
        self.encap = "@"

        
        
        try:
            self.sock.connect((self.host, self.port))
            print("\n[CONNECTED]\n")
        except Exception as e:
            print(e)
       
        

            
    def get_msg(self, **kwargs):
#        self.E = threading.Event()
        
        while True:
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("[RECV]: ", str(received), "\n")
                #return str(received)
            
                if not received:
                    return "WHAT_FO_DIS::NOT RECVD"
                else:

                    return str(received)
            except Exception as e:
                print("[SOCKET CLOSED]")
                print(str(e)) 
                self.sock.close()   
    
    
    def send_msg(self, data):
        msg = ""
        for _ in data:
            msg += str(_)
        try:
            self.sock.send(msg.encode())
            
        except Exception as e:
            print("FUCKUP::MSG_SEND::", str(e))
        return #str(self.get_msg())





