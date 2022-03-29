import socket
from _thread import *
from threading import Thread



class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.msgs = []
    
    
    def handle_client(self, conn, addr, mySocket):
        #mySocket.setblocking(False)
        print("[ADDR]: " + addr[0])

        while True:
            data = conn.recv(1024 * 2).decode()
            self.msgs.append(str(data))
            #strdata = str(data)
            #test_str = "RE::"+str(strdata)
            try:
                #conn.sendall(test_str.encode())
                #print(strdata)
                msg = str(self.msgs)
                conn.sendall(msg.encode())
            except Exception as e:
                print(e)    

            try:
                mySocket.close()
            except Exception as e:
                print(e)


    
    def handle_file():
        pass


    def Main(self):
        self.conns = set()
        CLient_List = []
        Thread_Count = 0
        print("ATTEMPTING: ")
        host = '127.0.0.42'
        port = 7071
        
        addr = (host, port)
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            mySocket.bind(('', port))
        except Exception as e:
            print(e)
        
        mySocket.listen(20)
        
        while True:

            #mySocket.setblocking(False)

            
            self.conn, self.addr = mySocket.accept()
            self.conns.add(self.conn)
            CLient_List.append(str(self.addr))
            for _ in CLient_List:
                print(":LIST:", _)
   
            if addr:
                Thread_Count += 1
                print("[THREADS]: ", Thread_Count)
            print ("Connection from: " + str(addr))
            message = 'Thank you connecting'
            self.conn.sendall(message.encode())
            
            try:
                # start a new thread that listens for each client's messages
                t = Thread(target=self.handle_client, args=(self.conn, self.addr, mySocket))
                # make the thread daemon so it ends whenever the main thread ends
                t.daemon = True
                # start the thread
                t.start()
                t_list = []
                t_list.append(t)
                for i in t_list:
                    print("THREADS: ", str(i))
            except Exception as e:
                print("THREAD ERROR: ", str(e))

 #           try:
 #               thread = start_new_thread((self.handle_client), (self.conn, self.addr, mySocket))
 #               thread.de
 #               self.conn.sendall(str(thread).encode())
 #           except Exception as e:
 #               print("ERROR ON THREAD:: ",str(e))


if __name__ == '__main__':
    s = server()
    s.Main()