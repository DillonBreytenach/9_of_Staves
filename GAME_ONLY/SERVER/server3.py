import socket
from _thread import *
from threading import Thread, ThreadError
import threading
from time import thread_time
from tokenize import group

#from file_handle_S import File_man


class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #CONNECTION VARS
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 8084
        self.addr = (self.host, self.port)
        
        
        #CLIENT VARS
        self.client_list = []
        self.group_list = []
        self.group = []


        
        #bASE VARS
        self.BUFFER_SIZE = 1024 * 4
        self.SEPARATOR = "@"

    def run_to(self, obj_, data):
        ##GET UPDATES
        ##SEND UPDATES TO ALL MEMBERS OF GROUP
        print("OBJ_Q: \n>>", obj_[0][1])
        print(">>", obj_[1][1])
        print("DATA TO SEND: ", data)
        conn1 = obj_[0][0]
        conn2 = obj_[1][0]
        conn1.send(data.encode())
        conn2.send(data.encode())



    def read_list(self, obj, data):
        self.RL = threading.Event()
        print("OBJ IN QUESTION:: ", obj)
        obj_q = []
        if obj:
            print("READING..")
   
            try:
                print("READING....")
                for i in self.group_list:
                    obj_q = i
                    print("READING_GROUP: ")
                    for j in i:
                        #print("CONNECTION: ", j)
                        if obj == j:
                            print("FOUND OBJ_Q")
                            self.run_to(obj_q, data)
            except Exception as e:
                print(f'READ_LIST_ERR:: {str(e)}')
                pass



    def parent_list(self, client):
        self.E = threading.Event()

        num = len(self.client_list)
        if num % 2:
            self.group_list.append(self.group)


        if len(self.client_list) >= 1:
            self.group.append(client)
            
            print(f'[CURRENT_GROUP]::')
            for _ in self.group:
                print(f'>> {str(_[1])}')


        if len(self.group) < 2:
            print('WAITING...')

            self.E.wait()

        elif len(self.group) == 2:
            self.group = []





    def check_list(self, client):
        for _ in self.client_list:
            if client == _:
                print(f'FOUND {str(_[1])}')
                return True
            else:
                print("FUCK_UP")




    def handle_client(self, conn, addr):
        #print("[ADDR]: " + str(addr))
        client = []
        client = [conn, addr]
        self.E = threading.Event()

        while True:
            try:

                data = conn.recv(1024 * 3).decode()
                if not data:
                    self.E.wait()
                else:
                    if "MSG" in data:
                        try:
                            print("___TESTING_IMPLEMENTATION___")
                            #CHECK LIST IF CLIENT EXISTS
                            if len(self.client_list) < 1:
                                print("STARTING")

                            if self.check_list(client) == True:
                                self.read_list(client, data)

                            else:
                                self.client_list.append(client)
                                grouping = threading.Thread(target=self.parent_list, args=(client,))
                                grouping.daemon = True
                                grouping.start()


                        except Exception as e:
                            print(f'BIG_KARADEO:: {str(e)}')
                            pass
                        

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

            except socket.error as e:
                print("[ERROR_CONNECTING_NEW_CLIENT] :", str(e))        
            
            try:
                t1 = threading.Thread(group=None, target=self.handle_client, args=(conn, addr))
                t1.daemon= True
                t1.start()
                
            except ThreadError as e:
                print(f'SERVER::MAIN:: {str(e)}')
                
                
                
if __name__=="__main__":
    s = server()
    s.Main()