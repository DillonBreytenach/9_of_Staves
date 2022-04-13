#LOGIN SCREEN
#BASE IMPORT
import profile
from telnetlib import TELNET_PORT
from threading import Thread
import threading
from kivy.app import App
import sys
from _thread import *
import string

#UIX IMOPORTS
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

#FUNTIONAL IMPORTS
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.metrics import dp

#CONNECTION__
import socket

from matplotlib.pyplot import connect
from numpy import size


#FILE HANDLE IMPORTS
from file_handle import File_man






class MainWidget(GridLayout):
    pass


class Login_Box(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        #LOGIN VARIABLES
        self.username = ""
        self.password = ""

        self.year = 0
        self.month = 0
        self.day = 0
        
        self.country = ""
        
        self.gender = ""

        self.file_name = ""
        
        #SETTUP VARIABLES
        self.encap = "CLIENT"
        
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

    def save_data(self):
        #self.data = (self.username, self.password, str(self.year), str(self.month), str(self.day), self.gender)
        self.convert()
        self.send_login()
    
    
    #CONVERT DATA
    def convert(self):
        self.data = str(self.encap + "@" + self.username + "@" + self.password + "@" + str(self.year) + "@" + str(self.month) + "@" + str(self.day) + "@" + self.gender)
        print("ENCAPPED: ", self.data)
        return self.data


    def check_data(self, data):
        print("CHECKING DATA: ", str(data))


        words = data.split("@")
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        print("[DATA_DECAPPED]: ")
        for _ in stripped:
            print(">", _) 
        

                
        if "CLIENT" in data:

            return "WELCOME " + str(stripped[1])

            




    
    #CONNECTION FUNCTIONS       
    def get_login(self, **args):
        while True:

            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                print("RECV: ", str(received))
                cd = self.check_data(received)
                

                if "WELCOME" in cd:
                    self.ids.in_com.text = cd
                else:
                    continue
            except Exception as e:
                print(str(e))
            if not received:
                print("MSG:", str(self.get_login()))
                break
            else:
                return str(received)
        self.sock.close()
                
    
    
    def send_login(self):
        try:
            msg = self.convert()
            self.sock.sendall(msg.encode())
        except Exception as e:
            print(e)
        return str(self.get_login())
    
    


     

class  ProfilePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile_data = []
    

    #PROFILE_LOADER

    def get_name(self, Widget):
        self.ids.Name.text = str(self.profile_data[1])


    
    def print_profile(self, data):
        print("DATA:@: PROFILE CLASS: ", data)
        self.profile_data = data
        print("PROFILE_NAME", self.profile_data[1])


class deck(ScrollView):
    pass

class Test(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Player_Variable
        self.profile = []
        
        self.orientation='lr-tb'
  
        #ENCAP
        self.encap = "GAME_BUTTON"
        
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
        
        
        
   
        
   #CONVERT DATA
    def convert(self, data):
        self.data = str(self.encap + "@" + data + "@" + "END")
        print("ENCAPPED: ", self.data)
        return self.data

        
    def check_data(self, data):
        print("CHECKING DATA: ", str(data))
        
        words = data.split("@")
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        
        print("[DATA_DECAPPED]:")
        for x in stripped:
            print(">",x)
        print("\n")
    
        if "DECK".upper() in stripped:
            print("DECAP", str(stripped[1]))
            deck = ""
            deck += str(stripped[1]) 
            
            return deck
        
        if "CLIENT".upper() in stripped:
            print("LOADING PROFILE: ", stripped[1])
            #self.profile = stripped
            ProfilePage.print_profile(self, stripped)

        
        #CONNECTION FUNCTIONS       
    def get_Test(self, **args):
        while True:

            received = ""
            try:
                received = self.sock.recv(1024 * 3).decode()
                
                data = self.check_data(received)
                
                print("RECV: ", str(data))
                #cd = self.check_data(received)
                return received
                #MAKE WIDGET_IMAGE FOR EACH CARD

            
            except Exception as e:
                print("GET_TEST", str(e))
            
            
            if not received:
                #self.sock.close()
                return "RETURN"#str(self.get_Test)
                
    
    
    def send_Test(self, data):
        try:
            msg = self.convert(data)
            self.sock.send(msg.encode())
        except Exception as e:
            print("SEND_TEXT", str(e))
        return str(self.get_Test())
    
 
      
    def print_deck(self, deck):
        root = StackLayout(orientation ='lr-tb')
        for i in deck:
            b = Button(text=str(i), size_hint=(None, None), size=(dp(100), dp(100)))
            root.add_widget(b)
        return root
        
        
        
    def test_button(self):
        Test_RE = ""
        print("TEST_BUTTON_PRESSED")
        Test_RE = Test.send_Test(self, "TEST_BUTTON")
        print("TEST_RE:  ", Test_RE)
        words = Test_RE.split("@")
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        root = StackLayout(orientation ='lr-tb')
        for i in stripped:
            b = Button(text=str(i), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
        
        
        
        
        
        
        
        stack = self.print_deck(stripped)    
        return stack





  
  
class Screen_Layout(PageLayout):          
    Login_Box()
    ProfilePage()
    Test()   

class Main(App):
    def Build(self):
        return Screen_Layout()


if __name__ == '__main__':
    Main().run()  
  