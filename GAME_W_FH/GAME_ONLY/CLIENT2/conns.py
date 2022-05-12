#CONNECTION__
import socket

import time
import sys

from file_handle_C import File_man
#import watchdog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

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

                if not received:
                    return "WHAT_FO_DIS::NOT RECVD"
                else:
                    return str(received)
            except Exception as e:
                print("[SOCKET CLOSED]")
                print(str(e)) 
                self.sock.close()   
    
    
    def send_msg(self):
        #READ ALL DATA FROM FILES>>
        path = "NAME.txt"
        
        self.init_data = str(self.FM.read_file(path))
        print("INIT_DATA:: ", self.init_data)
 
        try:
            while True:
                time.sleep(1)
                data = str(self.FM.read_file(path))
                print("SENDER DATA:: ", data)
                if self.init_data != data:
                    print(f'[SENDING]:: {data}')
                    self.init_data = data

                    try:
                        self.sock.send(data.encode())

                    except Exception as e:
                        print("FUCKUP::SEND_MSG::", str(e))

        except Exception as e:
            print("SENDING_ERROR::", str(e))
            #observer.stop()
            #observer.join()
        





