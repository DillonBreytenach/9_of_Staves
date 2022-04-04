#LOGIN SCREEN
#BASE IMPORT
from threading import Thread
import threading
from kivy.app import App
import sys
from _thread import *

#UIX IMOPORTS
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

#FUNTIONAL IMPORTS
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.clock import Clock

#CONNECTION__
import socket


#FILE HANDLE IMPORTS
from file_handle import File_man






class MainWidget(GridLayout):
    pass


class Login_Box(GridLayout):
#    import file_handle
#    from file_handle import File_man
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        #LOGIN VARIABLES
        self.username = ""
        self.password = ""
        #self.data = (self.username, self.password)
        self.file_name = ""
        self.encap = "CLIENT_1"
        
        #CONNECTION VARIABLES
        self.BUFFER_SIZE = 4096
        
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8081
        self.data = ""
        
        #CONNECTION INIT
        
        
        try:
            self.sock.connect((self.host, self.port))
            print("[CONNECTED]")
        except Exception as e:
            print(e)
        try:
            self.sock.bind((self.host, self.port))
            print("BOUND")
        except Exception as e:
            print("SOCKET NOT BOUND : ",str(e))
            
        try:
            self.sock.listen(5)
            self.sock.setblocking(False)
        except Exception as e:
            print(e)
        
        
        
        
        
        
        
    #LOGIN FUNCTIONS
    def save_name(self, Widget):
        self.username = Widget.text
    
    def save_password(self, Widget):
        self.password = Widget.text
                
    
    def save_data(self, Widget):
        self.data = (self.username, self.password)
        print("WRITING TO FILE", str(self.data))
        File_man.check_file()
        File_man.write_file(self, str(self.data))
        print("READING_FILE: ", File_man.read_file())
        msg = "HELLO"
        self.send_msg(msg)
        #self.send_msg()
    
    
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


    
    #CONNECTION FUNCTIONS       
    def get_msg(self, **args):
        
        while True:
            
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("RECV: ", str(received))
                cd = self.check_data(received)
                
                if cd == True:
                    print("NO TRANSIST PAGE TO CHAT SITE")
                else:
                    print("WTF")
                
                
                
            except Exception as e:
                print(str(e))
            if not received:
                print("MSG:", str(self.get_msg()))
                break
            else:
                return str(received)
        self.sock.close()
                
    
    
    def send_msg(self, hand):
        self.sock.send(hand.encode())
        try:
            msg = self.convert()
            self.sock.sendall(msg.encode())
        except Exception as e:
            print(e)
        return str(self.get_msg())
    

 
    def dev_input(self):
        pass
 
     

class BoxWidget(BoxLayout):
    pass

class Main(App):
    def Build(self):
        return Login_Box()


if __name__ == '__main__':
    Main().run()  
  