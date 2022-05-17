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
from gettext import translation
import string

from threading import Thread
import threading
import time
from unicodedata import name
from cv2 import sort
from kivy.app import App
from _thread import *


#FOLDER IMPORTS
from conns import connections
from file_handle_C import File_man


#UIX IMOPORTS
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, TransitionBase


#FUNTIONAL IMPORTS
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.clock import Clock


Window.size = (400, 300)



class Game(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "NAME_FUCK"
        self.my_deck = []
        self.opp_deck = []
        self.all_cards = []
        self.play_count = 0
        
        self.opp_hand = BoxLayout(size_hint=(.5, .4), pos_hint={'x': .3, 'y': .6})
        self.table = BoxLayout(size_hint=(.5, .4), pos_hint={'x': .3, 'y': .3})
        self.my_hand = BoxLayout(size_hint=(.5, .4), pos_hint={'x': .3, 'y': 0})

        self.add_widget(self.opp_hand)
        self.add_widget(self.table)
        self.add_widget(self.my_hand)

        self.FM = File_man()
        

        Clock.schedule_interval(self.fodis, .5)

    def hit_me(self, instance, data):
        print(self.name)
        self.FM.write_file("GAME.txt", str(str(data) + str(self.play_count)), "w")
            
        print("PLAY_COUNT:: ", str(self.play_count))
        self.play_count +=1


    def fodis(self, instance):
        #FM = File_man()
        print("FODIS::")
#        time.sleep(2)
        deck = self.FM.read_file("SERVER.txt")
        #print("DECK:: ", deck)
        if "DONE" in deck:
        
            self.FM.write_file("SERVER.txt", "", "w")

        deck_list = str(deck)
        card_set = deck_list.split("@")

        
        for i, card in enumerate(card_set):
            j = i+1
            #print("ITER:: ", card_set[i])
            if "MY" in card_set[i]:
                card_val = str(card_set[j])
                print("CARD_COMPARE:: ", card_val, self.my_deck)
                if card_val not in self.my_deck:
                    self.my_deck.append(card_set[j])
                

            if "OPP" in card_set[i]:
                if card_set[j] not in self.opp_deck:
                    self.opp_deck.append(card_set[j])
  
        self.display_cards()


    def display_cards(self):
        
        self.opp_hand.clear_widgets()
        self.table.clear_widgets()
        self.my_hand.clear_widgets()

        print("OPP_DECK: ", self.opp_deck)
        print("MY_DECK:  ", self.my_deck)

        for card in self.opp_deck:
            self.opp_hand.add_widget(Button(size=(.1, .4), text=str(card)))
            print(f'{card} made')
        
        for card in self.my_deck:
            self.my_hand.add_widget(Button(size=(.1, .4), text=str(card)))
            print(f'{card} made')


    def what_deck(self, what, data):
        
        #WRITE ALL SEND DATA TO FILE...

        self.FM.write_file("GAME.txt", str(str(data) + str(self.play_count)), "w")
            
        print("PLAY_COUNT:: ", str(self.play_count))
        self.play_count +=1
        



class Main_Widget(Screen):
    def __init__(self, **kwargs):
        super(Main_Widget, self).__init__(**kwargs)
        self.G = Game()
        self.FM = File_man()

    
    def p_it(self):
        #ALL INPUT FOR NAME
        #SAVE NAME TO FILE (NAME.TXT)
        name = ""
        name = str(self.ids.NAME.text)
        self.FM.write_file("NAME.txt", name, "w")
        self.FM.write_file("GAME.txt", "START", "w")
        self.FM.write_file("SERVER.txt", "@", "w")
        print("\n\nSTART_BUTTON_HIT\n\n")

        
        
class screen_manager(ScreenManager):
    Main_Widget()
    Game()


class Main(App):
    title = "9_of_Staves"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #IMPORT CONTROL
        self.FM = File_man()
        self.conn = connections()

        self.FM.write_file("GAME.txt", "", "w")
        self.FM.write_file("SERVER.txt", "", "w")


        self.recv = threading.Thread(target=self.conn.get_msg)
        self.watch = threading.Thread(target=self.conn.send_msg)


        try:
            self.recv.start()
            self.watch.start()

        except Exception as e:
            print(e)


    def Build(self):
        self.FM = File_man()
        sm = ScreenManager()
        return sm

if __name__ == '__main__':
    M = Main()
    M.run() 
