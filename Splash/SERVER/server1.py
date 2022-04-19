from curses.ascii import isalnum
import os
import socket
from _thread import *
from threading import Thread, ThreadError

import random
from random import shuffle
import threading
from file_handle_S import File_man



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
        
 
 
    """       
    def filter_data(self, got):
        data = ""
        data = str(got)
        words = data.split("@")
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        
        print("[DATA_DECAPPED]:")
        for x in stripped:
            print(">",x)
        print("\n")
        
        if "FUCK" in stripped:
            l = ["NONE", "?"]
            return "GOT_IT", l
        
        
        if "PROFILE" in stripped:
            print("READ::PROFILE??")
            re_data = File_man.read_file("clients/" + str(stripped[1]+".txt"))
            re_file = ["PROFILE"]
            file_line = re_data.split("\n")
            file_t = str.maketrans("", "", string.punctuation)
            file_strip = [ft.translate(file_t) for ft in file_line]
            
            for _ in file_strip:
                re_file.append(str(_))
                print(">>>>", _)
            return "PROFILE", re_file
        
        
        if "GAMEBUTTON" in stripped:
            cards = ["card1@", "card2@", "card3@", "card4@"]
            random.shuffle(cards)
            print("[CARDS]: ", cards)
            
            return "CARDS", cards



        if "LOGIN" in stripped:
            print("[GOT CLIENT]: ", data)
            print("[WRITING] :", stripped) 
            
            #user_auth
            #DO A STRING COMPARE TO SEE IF THE PASSWORD MATCHES
            # #####!*!*!*!*!*!

            f_check = File_man.check_file(str("clients/"+str(stripped[1])+".txt"))
            
            if f_check == True:
                seg = []
                print("ADD ENCAP FOR RETURN MSG!!]]]")
                for _ in stripped:
                    seg.append(str(_))
                    print("SEGs", _)
                seg.append("END")
                print("SEG: ", seg)
                return "CLIENT", seg
                
                
            if f_check == False:
                File_man.write_file("clients/" + str(stripped[1]+".txt"), stripped, 'a')
                print("CHECKING FILE:  \n   ", File_man.check_file("clients/" + str(stripped[1]+".txt")))
                return "CLIENT", stripped

        
            elif "READ".upper() in data:
                re_data = File_man.read_file("clients/" + str(stripped[1]+".txt"))
                print("PROFILE_NAME", re_data[1])
                return re_data 

            else:
                l = ["NONE", "?"]
                return "GOT_IT", l
    """         
        
        
    def check_data(self, data):
        words = data.split("@")
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        if not stripped:
            l = ["FUCK", "YOU"]
            return "FODIS", l
        try:
            print("[DATA_DECAPPED]:")
            for x in stripped:
                print(">",x)
            print("\n")
        except Exception as e:
            print(e)
            pass    
        
        if "PRO" in stripped[0]:
            try:
                re_data = ""
                f_name = str(stripped[1])
                print("READ::PROFILE??")
                fc = File_man.check_file("CLIENTS/" + str(f_name)+".txt")
                if fc == True:
                    re_data = File_man.read_file(("CLIENTS/" + str(f_name)+".txt"))
                    print("BEFORE STRIPPING::", re_data)
 #                   what = "\n"
#                    words = re_data.split("\n")
  #                  table = str.maketrans("", "", string.punctuation)
   #                 stripped = [w.translate(table) for w in words]
                    #print("CHECK_DATA RETURNING::", re_data)
                    return "PROFILE", re_data
        
                    
                if fc == False:
                    print("NOT_DATA_ON_FILE")
                    File_man.write_file(("CLIENTS/" + str(f_name)+".txt") , stripped, "w")
                    fC = File_man.check_file(("CLIENTS/" +str(f_name) +".txt"))
                    if fC == True:
                        re_data = File_man.read_file(("CLIENTS/" + str(f_name)+".txt"))
                          
                        
                        
                        return "PROFILE", stripped
        
            except Exception as e:
                print("DATA_HANDLER: ", str(e))    

        elif "MMO" in stripped:
            if "MMO" not in stripped:
                pass
            try:
                msg = []
                m_e = str(stripped[1])
                print("[SENDING]: ", m_e)
                msg = ["MMO@",m_e,"@END"]
                for _ in msg:
                    print("[MSG]: ", str(_))

                return "MMO", list(msg)            
            except Exception as e:
                print("DATA_HANDLER: ", str(e))
        

        
        
    

    #CONNECTION FUNCTIONS

    def handle_client(self, conn, addr, mySocket):
        print("[ADDR]: " + str(addr))
        action = ""
        fdata = []
        got = ""
        what = []
    
        while True:
            try:
                
                data = conn.recv(1024 * 3).decode()
                got = str(data)
            except Exception as e:
                print("[FAILED_TO_RECEIVE]: ", str(e)) 
            try:
                action, fdata = self.check_data(data)
                print("[ACTION]: ", str(action), "\n[CONTENT]: ")
                for _ in fdata:
                    print("F_DATA::", _)
                if "FODIS" in action:
                    return
                what = fdata
                for _ in what:
                    print("> ", str(_))
                #conn.send("FO_DIS: ".encode())
            except Exception as e:
                print("BS_FUCK_UP", str(e))
                

            if not action:
                print("[WAITING FOR CLIENT]")

            if "GOT_IT" in action:
                conn.send("GOT_IT".encode())


            if "CARDS".upper() in action:
                print("SENDING: CARDS ")

                print("[ACTION]: ", action)

                for _ in fdata:
                    print("CARD: ", _)
                    conn.send(str(_).encode())

            if "PROFILE" in action:
                mlist = ""
                
                print(f'SENDING:: {fdata}')
                for _ in fdata:
                    mlist += str(_)
                conn.send(mlist.encode())


            if "LOGIN" in action:
                seg = ""
                for _ in fdata:
                    print("SENDING_PROFILE: ", _)
                    seg += str(_+"@")
                conn.send(seg.encode())


#************************************************

            ##WILL USE FOR OPONENT PLAYERS
            if "MMO" in action:
                try:
                    print("@MMO>", fdata)
                    string = ""
                    for _ in fdata:
                        string += str(_)
                    try:
                        for x in self.CLient_List:
                            print("\n***\nCONNECTIONS: ", x)
                            if(x != conn):
                                try:
                                    x.sendall(str(string).encode())
                                except Exception as e:
                                    print("MMO_FUCKUP: ", str(e))
                    except Exception as e:
                        print("MMO_WTF:?", str(e))
                
                except Exception as e:
                    print("MMON_FUCK_UP: ", str(e))
                try:
                    conn.send("[SENT]".encode())
                except Exception as e:
                    print("[MSG_NOT_SENT] ::error::", str(e))

#************************************************


            try:
                if "DISCONN" in str(data):
                    mySocket.close()
            except Exception as e:
                print("\n!!!!!!\nCONN NOT CLOSED", str(e))




            if not data:
                print("\n!!!!!!!!\nNO DATA YET")
                return



  
  
    
    def Main(self):
        host = '127.0.0.1'
        port = 8083
        
        
        addr = (host, port)
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        Thread_Count = 0
        print("[SERVER RUNING]: ", str(host), str(port))
        
        try:
            mySocket.bind(('', port))
            print("[BINDING] ")
        except Exception as e:
            print("NOT BINDING: ", str(e))
        
        mySocket.listen(40)
        print("[SERVER LISTENING]:")
        
        while True:
            try:
                conn, addr = mySocket.accept()

                self.CLient_List.add(conn)
                print ("Connection from: " + str(addr))
                #for _ in self.CLient_List:
                #    print(":LIST:", str(_))
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