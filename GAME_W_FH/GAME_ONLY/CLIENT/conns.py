#CONNECTION__
import socket
import time
from file_handle_C import File_man

#CONNECTION CLASSES
class connections():
    def __init__(self, **kwargs):
        self.val = ""
        self.FM = File_man()
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8085
        self.encap = "@"

        
        
        try:
            self.sock.connect((self.host, self.port))
            print("\n[CONNECTED]\n")
        except Exception as e:
            print(e)
       
        

            
    def get_msg(self, **kwargs):
        #WRITE ALL DATA TO FILE
        while True:
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("[RECV]: ", str(received), "\n")
                self.FM.write_file("SERVER.txt", received, "a")

            except Exception as e:
                print("[SOCKET CLOSED]")
                print(str(e)) 
                self.sock.close()   
    
    
    def send_msg(self):
        #READ ALL DATA FROM FILES>>
        name = "NAME.txt"
        game = "GAME.txt"


        self.name_data = str(self.FM.read_file(name))
        self.game_data = str(self.FM.read_file(game))
        #    print(f'READING {file}')
        print("NAME_DATA:: ", self.name_data)
        print("GAME_DATA:: ", self.game_data)


        try:
            while True:

                self.N_data = str(self.FM.read_file(name))
                #print("SENDER DATA:: ", data)
                if self.name_data != self.N_data:
                    print(f'\nB[C]::{self.name_data}\n::\n[SENDING]:: {self.N_data} ')
                    
                    try:
                        self.name_data = self.N_data
                    except Exception as e:
                        print(e)
                    print(f'\nA[C]::{self.name_data}\n::\n[SENDING]:: {self.N_data} ')

                    try:
                        self.sock.send(str(self.N_data).encode())

                    except Exception as e:
                        print("FUCKUP::SEND_MSG::", str(e))


                G_data = str(self.FM.read_file(game))
                #print("SENDER DATA:: ", data)
                if self.game_data != G_data:
                    print(f'[SENDING]:: {G_data}')
                    self.game_data = G_data

                    try:
                        self.sock.send(G_data.encode())

                    except Exception as e:
                        print("FUCKUP::SEND_MSG::", str(e))







        except Exception as e:
            print("SENDING_ERROR::", str(e))






