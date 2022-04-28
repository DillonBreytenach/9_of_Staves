#BASE IMPORTS
from threading import Thread
import threading
from kivy.app import App
from _thread import *
#FOLDER IMPORTS
from conns import connections
from file_handle_C import File_man


#UIX IMOPORTS
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


#FUNTIONAL IMPORTS
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.window import Window


Window.size = (200, 250)



class Main_Widget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        File_man.__init__(self)
        self.encap = []
        self.FH = File_man()
        
        

    def get_name(self, Widget):
        self.encap = ["@", "NAME", "@", Widget.text]
        print(self.encap)
        self.FH.write_file("NAME.txt", self.encap, "w")
        print(self.FH.read_file("NAME.txt"))
        
    def read_name(self):
        return str(self.encap)
        


class Game(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = connections()
        self.M = Main_Widget()
        #self.cap = ""
        self.cap = self.M.encap
        
    def get_name(self):
        self.M.read_name()    
    
    def send(self, Widget):
        msg = ""
        msg = str(Widget.text)
        print("TO_SEND: ", msg)
        print("encap:: ", str(self.M.ids.NAME))
        data = str("MSG@" + msg)
        send = threading.Thread(target=self.c.send_msg, args=(data,))
        send.daemon = True
        send.start()
        
        
        recv = threading.Thread(target=self.get_)
        recv.daemon = True
        recv.start()
        
    def get_(self):
        while True:
            rec = self.c.get_msg()
            if rec:
                self.ids.in_com.text = rec
            else:
                print("WAITING")
            
        




class Page_Layout(PageLayout):

    Game()



class Main(App):
    title = "9_of_Staves"
    def Build(self):
        return Page_Layout()


if __name__ == '__main__':
    Main().run() 
