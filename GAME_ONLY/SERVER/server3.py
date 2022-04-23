import socket
from _thread import *
from threading import Thread, ThreadError
import threading

#from file_handle_S import File_man


class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 8084
        self.addr = (self.host, self.port)
        self.CLient_Set = set()
        self.CLient_List = []
        self.msg = []
        
        self.BUFFER_SIZE = 1024 * 4
        self.SEPARATOR = "@"


    def contacts(self, data):
        
        
        for j, _ in enumerate(self.CLient_List):
            print(f'\nC_LST::{_[0]}')
            con = _[0]
            try:
                con.send(data.encode())
            except socket.error as e:
                print(e)
        


    def handle_client(self, conn, addr):
        print("[ADDR]: " + str(addr))

        self.E = threading.Event()
        while True:
            try:
                
                data = conn.recv(1024 * 3).decode()
                if not data:
                    self.E.wait()
                else:
                    print(f'DATA:: {data}')
                    self.contacts(data)
            except Exception as e:
                print("[FAILED_TO_RECEIVE]: ", str(e)) 
    
    def Main(self):

 
        try:
            self.sock.bind(('', self.port))
            print("[BINDING] ")
        except Exception as e:
            print("NOT BINDING: ", str(e))
        
        self.sock.listen(40)
        print("[SERVER LISTENING]:")
        
        while True:
            try:
                conn, addr = self.sock.accept()

                client = [conn, addr]
                self.CLient_List.append(client)
                self.CLient_Set.add(conn)
                print(f'[CONNS COUNT] {threading.activeCount() -1}')
                print ("[Connection from]: " + str(addr))
                
                

            except socket.error as e:
                print("[ERROR_CONNECTING_NEW_CLIENT] :", str(e))        
            
            try:
                t1 = threading.Thread(group=None, target=self.handle_client, args=(conn, addr))
                #t1.daemon= True
                t1.start()
                
            except ThreadError as e:
                print(f'SERVER::MAIN:: {str(e)}')
                
                
                
if __name__=="__main__":
    s = server()
    s.Main()