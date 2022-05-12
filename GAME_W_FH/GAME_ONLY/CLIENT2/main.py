#TODO:
##MAKE TURN_BASES (PLAYER_1 THEN PLAYER_2)
###ACTIVATE/DEACTIVATE
##UI:
###LAYER 1:
    #BASE_LAYOUT: MOVE_BUTTONS(LEFT(.2, 1)), 
    #OPP_HAND(TOP(.7, .3)), 
    #TABLE_R(MID(.7, .3)),
    #MY_HAND(BOTTOM(.6, .3)), 
    #RIGHT(DATA(.2))
##THREAD CONTROL:
    #MAKE SINGULAR UPDATE FUNTION
    #WRITE ALL PLAYER INPUT TO FILE
    #SEND ALL DATA FROM READ FILE
    
#**  ##FILE_CONTROL:  ******
    ###TIMESTAMP AS FILE NAME
    ###LOOP_1: IF NEWEST C_TIME < FILE_TIME: #{"SEND"+str(TIME)+".txt"} 
            #READ ALL SEND(DATA) AND SEND TO SERVER
            
    ###LOOP_2: {"REC"+str(TIME)+".txt"}
            #READ ALL REC(DATA) AND UPDATE UI



#BASE IMPORTS
from functools import partial

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
from kivy.uix.screenmanager import ScreenManager, Screen


#FUNTIONAL IMPORTS
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.clock import Clock


Window.size = (400, 300)



class Game(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #FILE IMPORTS
        #self.c = connections()
        self.FM = File_man()
        
        #DECK VARIABLES
        self.my_deck = []
        self.opp_deck = []
        self.all_cards = []
        

                #CREATE ANCHOR LAYOUT:
        self.anch = BoxLayout(size_hint=(.6, 1))
        self.add_widget(self.anch)

    def get_(self):
    
    #GET_ALL_DATA_FROM_FILE
    
    
        card_set = []        
        
        while True:
            rec = self.c.get_msg()
            if "DONE" in rec:
                print("ALL CARDS_USED")
                self.anch.clear_widgets()

            card_set = list(rec.split("@"))
            print("CARD:SET:  ",card_set)
            self.all_cards.append(card_set)

            
            if "OPP" in rec:
                self.opp_deck.append(str(card_set[1]))
                print("OPP_DECK:: ", self.opp_deck)
                self.ids.OPP_DECK.text = str(card_set[1])

            if "MY" in rec:
                self.my_deck.append(str(card_set[1]))
                print("MY_DECK:: ", self.my_deck)            
                self.ids.MY_DECK.text = str(card_set[1])

            else:
                print("WAITING")
    
    def test(self, data, what):
        #GET CARD DATA FROM FILE (CARDS.TXT)
        #EVENT TRIGGERS USING WATCHDOG IMPORT
        
        
                #CREATE ANCHOR WIDGETS: FOR EACH CARD
        print("CARDS ON TABLE: \n >>", self.all_cards )

        self.anch.clear_widgets()


        for card_set in self.all_cards:
            if "OPP_CARD" in card_set:
                print("OPP's:  ", card_set)
                c_card = Button(text=card_set[1], pos_hint={'x': 0, 'y': .5}, size_hint=(.4, .3))
                self.anch.add_widget(c_card)
            
            if "MY_CARD" in card_set:
                print("MY's:   ", card_set)
                c_card = Button(text=card_set[1], pos_hint={'x': 0, 'y': 0}, size_hint=(.4, .3))
                self.anch.add_widget(c_card)



    def what_deck(self, data, what):
        #WRITE ALL SEND DATA TO FILE...
        
        #self.FM.write_file("GAME.txt", data, "w")
        
        deck = list(self.FM.read_file("GAME.txt"))
        print("DECK ON GAME.txt::::  ", deck)
        Clock.schedule_once(partial(self.test, ("init")), 0)

        print(f'WHAT_DECK:\n    : {what}\n')
        print(f'WHAT_DATA:\n    : {data}\n')

        deckin = "CARD"
        deck = str(deckin)
        self.send = threading.Thread(target=self.c.send_msg, args=(deck,))
        self.recv = threading.Thread(target=self.get_)
        

        self.send.daemon = True
        self.recv.daemon = True
        
        self.send.start()
        self.recv.start()




class Main_Widget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.G = Game()
        self.FM = File_man()

        #self.conn = connections()
        #watch = threading.Thread(target=self.conn.send_msg)
        #watch.daemon = True
        #watch.start()





        
    def p_it(self):
        name = ""
        name = str(self.ids.NAME.text)
        data = [name]
        self.FM.write_file("NAME.txt", data, "w")
        #ALL INPUT FOR NAME
        #SAVE NAME TO FILE (NAME.TXT)
        #MAKE BUTTON SWITCH SCREEN TO GAME SCREEN
        print("START_BUTTON_HIT:\n:: DOES NOTHING")


class Page_Layout(PageLayout):
    Main_Widget()
    Game()



class Main(App):
    title = "9_of_Staves"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.conn = connections()
        watch = threading.Thread(target=self.conn.send_msg)
        watch.daemon = True
        watch.start()
        
    
    def Build(self):
        self.FM = File_man()


        self.screen_manager = ScreenManager()
        
        self.Game_Page = Game()
        screen = Screen(name="Game")        
        screen.add_widget(self.Game_Page)
        self.screen_manager.add_widget(screen)
        
        self.Main_Widget = Main_Widget()
        screen = Screen(name="Main_Widget")
        screen.add_widget(self.Main_Widget)
        self.screen_manager.add_widget(screen)



        return self.screen_manager


if __name__ == '__main__':
    M = Main()
    M.run() 
