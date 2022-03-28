#LOGIN SCREEN
#BASE IMPORT
from lib2to3.pytree import convert
from kivy.app import App

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
        self.port = 7000
        self.data = ""
        self.text_in = StringProperty("")
        try:
            self.sock.connect((self.host, self.port))
        except Exception as e:
            print(e)
        #self.sock.bind(self.host, self.port)
        try:
            self.sock.listen()
        except Exception as e:
            print(e)    
    def get_msg(self):
        try:
            self.received = self.sock.recv(1024).decode()
        except Exception as e:
            print(e)
            # self.sock.close()
    
        return str(self.received)
    
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
        self.data = str(self.text_in)
        return self.data

    #--------------------------------

    def get_text(self):
        print(self.received)
        self.ids.in_com.text = self.received
        return str(self.received)

    
    def on_click(self):
        try:
            print("[BUTTON_CLICKED]")  
            print("TEXT: " + str(self.text_in))
            self.send_msg()
            
            self.ids.in_com.text = self.received
        except Exception as e:    
            print(e)
     #VARS
    
    #FUNCTION defs
    def set_text(self, widget):
        self.text_in = widget.text
        print("[MSG]: " + self.text_in)




class PageLayout_(PageLayout):
    pass


"""
class Login_Widget(BoxLayout):
    try:
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.orientation = 'vertical'
        
    except Exception as e:
        print(e)
    
    
    

    
    #CONNECTION
class BoxWidget(BoxLayout):
    s = socket.socket()
    host = '127.0.0.1'
    port = 7000
    display = ObjectProperty()


    def connect_to_server(self):
        # called by a Button press

        # Connects to the server
        self.s.connect((self.host, self.port)) 

        # Receives confirmation from Server
        data = self.s.recv(1024).decode()      

        # Converts confirmation to string
        strdata = str(data)                     

        # Prints confirmation
        print(strdata)                                   

    def send_message(self):    
        # Is called by the function below
        # Encodes and sends the message variable                  
        self.s.send(self.message.encode()) 

        # Waits for a reply   
        self.receive_message()                     

    def message_to_send(self):  
        # Defines Message to send                 
        self.message = self.display.text
        # Calls function to send the message                
        self.send_message()     

    # Note
    # When I used message = input directly in send_message,
    # the app would crash. So I defined message input 
    # in its own function which then calls the 
    # send function  

    # message_to_send is the function actually
    # called by a button press which then
    # starts the chain of events
    # Define Message, Send Message, get Reply

    def receive_message(self):
        # Decodes a reply                    
        reply = self.s.recv(1024).decode()

        # Converts reply to a str
        strreply = str(reply)

        # prints reply
        print(strreply)
"""        
        
        

"""

class ServerApp(App):    
     def build(self):
          box = BoxWidget()
          return box
"""

class Main(App):
    pass

if __name__ == '__main__':
    Main().run()  
  