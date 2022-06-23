import socket
from _thread import *
import string
from threading import Thread, ThreadError
import threading
#from file_handle_S import File_man #NOT YET IN USE
from deck import Deck



class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #INITS
        self.D = Deck()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 8085
        self.addr = (self.host, self.port)


        #ADD MAP for CLIENT PROFILES, 

        #CLIENT VARS
        self.group_num = 0
        self.client_list = []
        self.group_list = []
        self.group = []
        
        
        self.CLIENT_LIST = []
        #group = 0
        #conn = ""
        #addr = ""
        #client = [conn, addr]
        #active = ""
        #member_obj = [client, active]
        #cmd = ""
        #card = ""
        #wid = ""
        #action = [cmd, card, wid]

        
        
        #
        self.CLIENT_GROUPS = []




        #bASE VARS
        self.BUFFER_SIZE = 1024 * 6





    def filter_change(self, data, change):
        if "HAND" in change:
            filt = data.split("@")
            print("\nFILTER\n::->>", change)
            new_data = ""
            for _ in filt:
                val = _.translate(str.maketrans('','',string.punctuation))
                print("VAL::",val)
                new_data += str(val)+"&"
            return(new_data)
        
        if "TABLE" in change:
            print("TABLE:: ", data)
            return("NONE")
        
        if "ELEM" in change:
            return("NONE")





    def run_to(self, group_obj, obj1, obj2, obj, data):
        ##GET UPDATES

        ##SEND UPDATES TO ALL MEMBERS OF GROUP
        obj_q = str(obj[0])
        print("\nRUN_TO_DATA: \n",obj_q,"\n     >>", data)
        print("\nRUN_TO:: _OBJs \n", ">>::OBJ_1::\n", obj1, "\n>>::OBJ_2::\n", obj2)



        #INIT_ACTIVE_GAME_DATA
        if "MATCH" in data:
            obj1.send("MATCH1@".encode())
            obj1.send("DECK@".encode())
            
            obj2.send("MATCH2@".encode())
            obj2.send("DECK@".encode())
            
            DECK = ["DECK@",]
            self.D.shuffleDeck()
            cards = self.D.Deck_List
            
            
            for card in cards:
                DECK.append("CARD&"+card+"@")

            for card in DECK:
                obj1.send(card.encode())
                obj2.send(card.encode())
            print("DECK_SENT\n**")
            obj1.send("SET".encode())
            obj2.send("SET".encode())










        if "HAND" in data:
            s_data = str(data)
            l_data = s_data.split("@")
            print("RED_HANDEDATA::", s_data)
            msg = ""
            for _ in l_data:
                if len(_) > 1:
                    msg += _.translate(str.maketrans('','', "[,],',!,@,#")) #
                    msg += "@"


            print("MSG_TO_SEND_:: >>>>>>", msg)
            if str(obj[0]) == str(obj1):
                print("SENDING...", msg)
                obj2.send(msg.encode())
            if str(obj[0]) == str(obj2):
                print("SENDING...", msg)
                obj1.send(msg.encode())
        
        
        if "TABLE" in data:
#            print("!!!!\n\nTABLE\n\n!!!!\n::", data)

            s_data = str(data)
            l_data = s_data.split("@")
            print("TABLE_LAY'N_DATA::", s_data)
            msg = ""
            for _ in l_data:
                if len(_) > 1:
                    msg += _.translate(str.maketrans('','', "[,],',!,@,#")) #
                    msg += "@"


            print("MSG_TO_SEND_:: >>>>>>", msg)
            if str(obj[0]) == str(obj1):
                print("SENDING...", msg)
                obj2.send(msg.encode())
            if str(obj[0]) == str(obj2):
                print("SENDING...", msg)
                obj1.send(msg.encode())
        



        if "ELIM" in data:
            s_data = str(data)
            l_data = s_data.split("@")
            print("TABLE_LAY'N_DATA::", s_data)
            msg = ""
            for _ in l_data:
                if len(_) > 1:
                    msg += _.translate(str.maketrans('','', "[,],',!,@,#")) #
                    msg += "@"


            print("MSG_TO_SEND_:: >>>>>>", msg)
            if str(obj[0]) == str(obj1):
                print("SENDING...", msg)
                obj2.send(msg.encode())
            if str(obj[0]) == str(obj2):
                print("SENDING...", msg)
                obj1.send(msg.encode())
        






    def read_list(self, obj, data):
        #FIND CLIENT IN GROUP >> SEND DATA in RUN_TO
        #[#, [[[conn, addr],active], [data]]]
        print("READ_LIST:\n:CLIENT IS HERE  \n>>", obj[1])
        self.RL = threading.Event()

        obj1 = []
        obj2 = []

        if obj:
            print("READING CLIENT LIST..")
            try:
                #FIND THE MATCHING ADDR in GROUP NUM_VAL
                for i, group_obj in enumerate(self.CLIENT_GROUPS):
                    print("OBJ_IN_Q:: ::", str(i))
                    for j, cl in enumerate(group_obj):
                        if len(cl) == 1:
                            print("GROUP>>", cl, "\n", j, "\n")
                        if len(cl) >= 2:
#                            print("j", j,
#                                  "\n[CONN]:  ", 
#                                  str(cl[0][0]), 
#                                  "\n[ADDR]: ",
#                                  str(cl[0][1]),
#                                  "\n[ACTIVITY]: ", 
#                                  str(cl[1]))

                            obj1 = group_obj[1][0][0]
                            obj2 = group_obj[2][0][0]
                            #print(f"\n*********\nobj_1: {obj1}\nobj_2: {obj2}\n")
                try:
                    self.run_to(group_obj, obj1, obj2, obj, data)
                    print("RUNN__TO:: obj[1] ", str(obj[1]))
                except Exception as e:
                    print("RUN_TO_ERROR :: ", str(e))
            except Exception as e:
                print(f'READ_LIST_ERR:: {str(e)}')
                pass




    #CREATE ACTIVE GAME GROUPS
    def parent_list(self, client, data):
        self.E = threading.Event()


        if len(self.group) <= 1:
            self.group.append(client)

        if len(self.group) < 2:
            print('WAITING...FOR OPP')
            self.E.wait()

        #INIT GROUP NUMBER >> APPEND MEMEBERS TO GROUP
        if len(self.group) == 2:
            group_obj = [[self.group_num],]
            #CREAT_GROUP_OBJ
            #print("[CURRENT_GROUP]:: ", self.group_num)
            for cl in self.group:
                mem_obj = [cl, "ACTIVE"]
                group_obj.append(mem_obj)

            self.CLIENT_GROUPS.append(group_obj)
            self.group_num +=1
            self.group = []
            self.read_list(client, "MATCH")
            print("MATCH_MADE::PARENT_LIST")

            





    def check_list(self, client):
        try:
            print("\n\nCHECKING...CLIENT...:\n")
            if len(self.CLIENT_LIST) < 1:
                return False
            for _ in self.CLIENT_LIST:  
                print("$$_ACTIVE_CLIENTS::\n    ls>>", str(_[1]), "\n    cl>>", str(client[1]))      
                if str(client[1]) == str(_[1]):
                    print(f'FOUND {str(_[1])}\n')
                    return True
                else:
                    print("NO_SUCH_CLIENT:: \n", str(_[1]))
                    return False
        except Exception as e:
            print(str(e), "CHECK_LIST")



    def handle_client(self, conn, addr):
        print("conn...", addr)
        client = []
        client = [conn, addr]
        self.E = threading.Event()


        #self.CLIENT_LIST.append(client)
        while True:
            try:

                data = conn.recv(1024 * 6).decode()
                if not data:
                    self.E.wait()

                else:
                    
                    print("msg..", data, " BY ", addr)
                    if "HAND" in data:
                        print("****\nHAND\n****")
                        try:
                            #if self.check_list(client) == True:
                            self.read_list(client, data)
                        except Exception as e:
                            print("HAND_ERROR::", str(e))
                     
                     
                    if "TABLE" in data:
                        print("****\nTABLE\n****")
                        try:
                            #if self.check_list(client) == True:
                            self.read_list(client, data)
                        except Exception as e:
                            print("HAND_ERROR::", str(e))
                     
                     
                                      
                                      
                    if "ELIM" in data:
                        try:
                            self.read_list(client, data)
                        except Exception as e:
                            print("ELIM_ERROR", str(e))       
                    
                    if "START" in data:
                        try:
                            #CHECK LIST IF CLIENT EXISTS
                            if len(self.CLIENT_LIST) == 1:
                                print("\n**FIRST_CLIENT", str(self.CLIENT_LIST[0]))
                                

                            if self.check_list(client) == True:
                                self.read_list(client, data)

                            else:
                                self.CLIENT_LIST.append(client)
                                #print("NEW CLIENT ADDED:: \n", addr, "\n-----------------\n")

                                grouping = threading.Thread(target=self.parent_list, args=(client, data))
#                                grouping.daemon = True
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
        print("[LISTENING]:")
        
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