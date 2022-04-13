import os
import socket
from _thread import *
from threading import Thread, ThreadError

import random
from random import shuffle


import string

from matplotlib.pyplot import table


from file_handle_S import File_man

import tqdm

class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.CLient_List = set()
        self.msg = []
        
        self.BUFFER_SIZE = 1024 * 4
        self.SEPARATOR = "@"
        
        
    def filter_data(self, data):
        words = data.split("@")
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        ##
        print("[DATA_DECAPPED]:")
        for x in stripped:
            print(">",x)
        print("\n")
        
        if stripped[0] == "GAMEBUTTON":
            cards = ["card1@", "card2@", "card3@", "card4@"]
            random.shuffle(cards)
            print("[CARDS]: ", cards)
            
            return "CARDS", cards



        if "CLIENT" in data:
            print("[GOT CLIENT]: ", data)
            print("[WRITING] :", stripped) 
            
            #user_auth
            #DO A STRING COMPARE TO SEE IF THE PASSWORD MATCHES
            # #####!*!*!*!*!*!

            f_check = File_man.check_file(str("clients/"+str(stripped[1])+".txt"))
            
            if f_check == True:
                print("ADD ENCAP FOR RETURN MSG!!]]]")
                for _ in data:

                    seg = str(_) + "@"
                    print("SEGs", _)
                print("SEG: ", seg)
                return "CLIENT", stripped
                
                
            if f_check == False:
                File_man.write_file("clients/" + str(stripped[1]+".txt"), stripped, 'a')
                print("CHECKING FILE:  \n   ", File_man.check_file("clients/" + str(stripped[1]+".txt")))
                return "CLIENT", stripped

        
        elif "READ".upper() in data:
            re_data = File_man.read_file("clients/" + str(stripped[1]+".txt"))
            return re_data          
    
    
    #CONNECTION FUNCTIONS

    def handle_client(self, conn, addr, mySocket):
        print("[ADDR]: " + str(addr))
        
    
        while True:
            data = conn.recv(1024 * 3).decode()
            print("\n[DATA]: ", str(data))
            
            action, fdata = self.filter_data(data)


            if not action:
                print("[WAITING FOR CLIENT]")


            if "CARDS".upper() in action:
                print("SENDING: CARDS ")

                print("[ACTION]: ", action)

                #conn.send(str(action).encode())
                for _ in fdata:
                    print("CARD: ", _)
                    conn.send(str(_).encode())


            if "CLIENT" in action:
                for _ in fdata:
                    print("PROFILE: ", _)
                    seg = str(_)
                    conn.send(seg.encode())


            try:
                if "DISCONN" in str(data):
                    mySocket.close()
            except Exception as e:
                print("\n!!!!!!\nCONN NOT CLOSED", str(e))




            if not data:
                print("\n!!!!!!!!\nNO DATA YET")
                return


#            else:
#                
#                try:
#
#                    conn.send("GOT_DATA**".encode())
#                    
#                    #m_len = len(self.msg)
#                    #self.msg.append(str(data))
#                    #sending = self.msg[(m_len)]
#
#                except Exception as e:
#                    print("WTF", str(e))



                    ##WILL USE FOR OPONENT PLAYERS
#                    try:
#                        for x in self.CLient_List:
#                            if(x != conn):
#                                try:
#                                    x.sendall(''.encode())
#                                except Exception as e:
#                                    print(e)
#      
#_-------------------------------------------_______-____-____________---------



#                            print("[MSG_SENT]: ", sending)
#                    except Exception as e:
#                        print("[SEND_ALL_FAIL] : ", str(e))
#                except Exception as e:
#                    print("CLIENT_HANDLE:", str(e))    
#    
  
  
  
    
    def Main(self):
        host = '127.0.0.1'
        port = 8081
        
        
        addr = (host, port)
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        Thread_Count = 0
        print("SERVER RUNING: ")
        
        try:
            mySocket.bind(('', port))
            print("BINDING: ", mySocket)
        except Exception as e:
            print("NOT BINDING: ", str(e))
        
        mySocket.listen(40)
        print("SERVER LISTENING:")
        
        while True:
            try:
                conn, addr = mySocket.accept()

                self.CLient_List.add(conn)
                print ("Connection from: " + str(addr))
                print(":LIST:", self.CLient_List)
            except socket.error as e:
                print("[ERROR_CONNECTING_NEW_CLIENT] :", str(e))        
            
            
   
            if addr:
                Thread_Count += 1
                print("[THREADS]: ", Thread_Count)
            
            try:
                # start a new thread that listens for each client's messages
                t = Thread(target=self.handle_client, args=(conn, addr, mySocket))
                # make the thread daemon so it ends whenever the main thread ends
                t.daemon = True
                # start the thread
                t.start()
                
               
            except ThreadError as e:
                print(e)


if __name__ == '__main__':
    s = server()
    s.Main()