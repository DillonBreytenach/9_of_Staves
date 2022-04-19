import socket
from _thread import *
from threading import Thread, ThreadError
from file_handle_S import File_man

class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.CLient_List = set()
        self.msg = []
    
    def check_data(self, data):
        if data:
            re = ["DONE", 0]
            return re
    
    def handle_client(self, conn, addr, mySocket):
        print("[ADDR]: " + str(addr))
    
        while True:
            data = conn.recv(1024 * 3).decode()
            print("DATA: ", str(data))

            checked_data = self.check_data(data)
            for _ in checked_data:
                if str(_) == "DONE":
                    continue
                else:
                    print(["CHECKED_DATA:", _])
                


            try:
                if str(data) == "DISCONN":
                    print("[CLOSING CONNECTION]")
                    mySocket.close()
            except Exception as e:
                print("CONN NOT CLOSED", str(e))

            try:
                if str(data) == "HELLO":
                    re = "HI, THERE"
                    print(re)
                    conn.send(re.encode())
                else:
                    conn.send("FU_DIS".encode())
            except Exception as e:
                print("FUCQ_ME")
                print(e)



            if not data:
                print("NO DATA YET")
                return
            else:
                
                try:

                    sending = self.msg


                    try:
                        for cs in self.CLient_List:
                            #print("cs: ", cs)
                            conn.send(sending.encode())
                    
                        print("[MSG_SENT]: ", sending)
                    except Exception as e:
                        print("[SEND_ALL_FAIL] : ", str(e))
                except Exception as e:
                    print(str(e))    




    
    def handle_file():
        pass


    def Main(self):
        host = '127.0.0.2'
        port = 8083
        
        
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
                for _ in self.CLient_List:
                    print("[CONNECTION]:[LIST]: \n", str(_))
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