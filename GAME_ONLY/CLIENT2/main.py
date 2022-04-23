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


class Main_Widget(Widget):
    pass


class Game(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = connections()
        
    def send(self, Widget):
        data = Widget.text
        print("TO_SEND: ", data)
        self.ids.in_com.text = self.get_(data)
        
    def get_(self, data):
        self.c.send_msg(data)
        self.E = threading.Event()
        in_com = self.c.get_msg()
        if not in_com:
            self.E.wait()
        else:
            return in_com





class Page_Layout(PageLayout):

    Game()



class Main(App):
    title = "9_of_Staves"
    def Build(self):
        return Page_Layout()


if __name__ == '__main__':
    Main().run() 
