#CONNECTION__
import socket


#CONNECTION CLASSES
class connections():
    def __init__(self, **kwargs):

       
        
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
        while True:
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("[RECV]: ", str(received), "\n")

            except Exception as e:
                print(str(e))
            if not received:
                return "WHAT_FO_DIS::NOT RECVD"
            else:
                self.sock.close()
                print("[SOCKET CLOSED]")
                return str(received)
                
    
    
    def send_msg(self, data):
        msg = ""
        for _ in data:
            msg += str(_)
        try:
            self.sock.send(msg.encode())
            
        except Exception as e:
            print("FUCKUP::MSG_SEND::", str(e))
        return str(self.get_msg())





