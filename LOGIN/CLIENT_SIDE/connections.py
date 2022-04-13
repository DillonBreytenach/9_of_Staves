#CONNECTION FOR LOGIN HANDLE
#CONNECTION FOR USER DATA
#CONNECTION FOR GAMEPLAY


import socket
from _thread import *
from threading import Thread

from file_handle_C import File_man





class connections():

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        
        
        
        
        
    #LOGIN FUNCTIONS
    def save_name(self, data):
        self.username = data
        print("USER_NAME SAVED")
    
    def save_password(self, data):
        self.password = data
        print("PASSWORD SAVED")
    
    def save_data(self, data):
        connections.send_login(connections.__init__, data)
    
    
    #CONVERT DATA
    def convert(self):
        self.data = str(self.encap + "@" + self.username + "@" + self.password)
        print("ENCAPPED: ", self.data)
        return self.data


    def check_data(self, data):

        
        print("CHECKING DATA: ", str(data))
        if data:
            
            return True
        pass





    
    #CONNECTION LOGIN FUNCTIONS       
    def get_login(self, **kwargs):
        
        
        
        
        while True:
            
            received = ""
            try:
                try:
                    received = connections.__init__.sock.recv(1024 * 3).decode()
                except Exception as e:
                    print("GET_LOGIN::SOCK::RECV :: ", str(e))
                    break
                print("RECV: ", str(received))
                cd = connections.check_data(connections.__init__, received)

                
                if cd == True:
                    print("NO TRANSIST PAGE TO PROFILE")
                    

                else:
                    print("WTF")
                
                
                
            except Exception as e:
                print("GET_LOGIN", str(e))

            if received:
                self.sock.close()
                return str(received)
                
                
    
    
    def send_login(self, data):
        print("SENDING: ", data)
        try:
            #msg = connections.convert(self)
            connections.__init__.sock.sendall(data.encode())
        except Exception as e:
            print("SEND_LOGIN", str(e))
        return str(connections.get_login(connections.__init__))
    


#PROFILE HANDLE -->>