#BASE IMPORTS
from threading import Thread
import threading
from kivy.app import App
from _thread import *
from conns import connections


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


Window.size = (400, 450)



class Main_Widget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encap = ""
        self.c = connections()

    def get_name(self, Widget):
        self.encap = "@NAME@"+Widget.text
        self.c.send_msg(self.encap)


class Game(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = connections()
        self.encap = ""

        
    def send(self, Widget):
        data = Widget.text
        print("TO_SEND: ", data)
        
        
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
