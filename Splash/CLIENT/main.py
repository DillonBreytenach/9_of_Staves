#CONNECTION__
from re import S
import socket
from threading import Thread
import threading
from kivy.app import App
import sys
from _thread import *
from kivy.clock import Clock

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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp



Window.size = (300, 450)






#APP CLASSES

class main_widget(BoxLayout):
    def __init__(self, **kwargs):
        self.data = "INIT"



class Login_Page(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = ""
        self.year = 0
        self.month = 0
        self.day = 0
        self.gender = ""
        self.profile = [self.name, self.year, self.month, self.day, self.gender]
        
        

    #LOGIN FUNCTIONS
    def save_name(self, Widget):
        
        self.username = Widget.text
        print(f'USERNAME: {self.username}')
    
    
    def save_password(self, Widget):
        self.password = Widget.text
        print(f'USERNAME: {self.password}')
        
        
    def save_year(self, Widget):
        self.year = int(Widget.text)
        print("YEAR: ", str(self.year))
        
    def save_month(self, Widget):
        self.month = int(Widget.text)
        print("MONTH: ", str(self.month))
        

    def save_day(self, Widget):
        self.day = int(Widget.text)
        print("DAY: ", str(self.day))
        

    def save_country(self, Widget):
        self.country = Widget.text
        print("COUNTRY: ", self.country)


    def CheckBox_M(self, value):
        print("VALUE:: MALE", value)
        if value == True:
            self.male_c = BooleanProperty(True)
            self.female_c = BooleanProperty(False)
            self.gender = "MALE"

    
    def CheckBox_F(self, value):
        print("VALUE:: FEMALE", value)
        if value == True:
            self.female_c = BooleanProperty(True)
            self.male_c = BooleanProperty(False)
            self.gender = "FEMALE"

    def convert(self):
            self.data = str("LOGIN" + "@" + self.username + "@" + self.password + "@" + str(self.year) + "@" + str(self.month) + "@" + str(self.day) + "@" + self.gender)
            print("[ENCAPPED]: ", self.data)
            return self.data


    def save_data(self):
        self.convert()
        self.send_login()
        
    def send_login(self):
        c = connections()
        c.send_msg(self.profile)


class Profile_Page(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile = ["PROFILE", "@", "NAME", "@", "AGE", "@", "COUNTRY"]
        t = threading.Thread(group=None, target=self.get_)
        t.daemon = True
        t.start()
        
    def clean_data(self, data):
        print("PRE_CLEANING: ", data)
        


    def get_(self):
        while True:
            c = connections()
            incom = c.get_msg()
            print("[IN_COM(s)]:", incom)
            self.clean_data(incom)
            self.ids.Opponent_One.text = str(incom)
    
    def data_sending(self, Widget):
        c = connections()
        msg = str("MMO@"+str(Widget.text))
        print("[MSG_OUT]: ",msg)
        fo_dis = c.send_msg(msg)
        print("FO_DIS:: ", fo_dis)
        print("ATTEMPT: get_msg()", connections.get_msg)

    def display_profile(self):
        c = connections()
        fo_dis = c.send_msg(self.profile)
        print("FODIS: ", fo_dis)
        self.ids.Opponent_One.text = str(fo_dis)
        re_msg = connections.get_msg(self)
        print("ATTEMPT: get_msg()", re_msg)



#CONNECTION CLASSES
class connections():
    def __init__(self, **kwargs):

       
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8083
        self.encap = "@"

        
        
        try:
            self.sock.connect((self.host, self.port))
            print("\n[CONNECTED]\n")
        except Exception as e:
            print(e)
       
        


    def check_data(self, data):

        print("CHECKING DATA: [!] ", str(data))
        return "done"

            
    def get_msg(self, **kwargs):
        while True:
            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("[RECV]: ", str(received), "\n")
                cd = self.check_data(received)
                print("[CHECKED_DATA]", cd, "\n")
                
            except Exception as e:
                print(str(e))
            if not received:
                return self.get_msg()
            else:
                return str(received)
        self.sock.close()
        print("[SOCKET CLOSED]")
                
    
    
    def send_msg(self, data):
        msg = ""
        for _ in data:
            msg += str(_)
        try:
            self.sock.send(msg.encode())
            
        except Exception as e:
            print("FUCKUP", str(e))
        return str(self.get_msg())


    def update(self):

        t = threading.Thread(target=self.get_msg)
        t.daemon = True
        t.start()

    






class Page_Layout(PageLayout):
    #connections()
    main_widget()
    Profile_Page()



class MainApp(App):
    title = "9_of_Staves"
    
    def Build(self):
        return Page_Layout()


if __name__ == '__main__':
    MainApp().run() 
