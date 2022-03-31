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


#LAYOUT_CLASSES

class MainWidget(GridLayout):
    pass
            

class Second_Box(ScrollView):
    
    #CONNECTION
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8080
        self.data = ""
        self.text_in = StringProperty("")
        self.encap = "CLIENT_1@"

        
        
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
    received = ""
        
        
    def update(self):
        
        t = threading.Thread(target=self.get_msg)
        t.daemon = True
        t.start()


    def check_data(self, data):

        print("CHECKING DATA: ", str(data))
        pass

            
    def get_msg(self, **kwargs):
        while True:
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("RECV: ", str(received))
                self.check_data(received)
                self.ids.in_com.text = received
            except Exception as e:
                print(str(e))
            if not received:
                print("MSG:", str(self.get_msg()))
                break
            else:
                return str(self.received)
        self.sock.close()
                
    
    
    def send_msg(self):
        try:
            msg = self.convert()
            self.sock.sendall(msg.encode())
        except Exception as e:
            print(e)
        return str(self.get_msg())
    
    
    #-----------END OF CONNECTION---

    #CONVERT DATA
    def convert(self):
        self.data = str(self.encap + self.text_in)
        return self.data

    #--------------------------------

    
    def on_click(self):
        try:
            #self.set_text(widget)
            print("[BUTTON_CLICKED]")  
            print("TEXT: " + str(self.text_in))
            self.send_msg()

        except Exception as e:    
            print(e)

     #VARS
    
    #FUNCTION defs
    def set_text(self, widget):
        self.text_in = widget.text
        
        print("[MSG]: " + self.text_in)
        self.data = str(self.text_in)
        


class PageLayout_(PageLayout):
    pass



class Main(App):
    pass

if __name__ == '__main__':
    Main().run()  
  