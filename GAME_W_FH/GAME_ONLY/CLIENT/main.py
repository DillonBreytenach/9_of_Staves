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
    
#@#THREAD CONTROL:
    #MAKES SINGULAR UPDATE FUNTION
    #WRITES ALL PLAYER INPUT TO FILE
    #SENDS ALL DATA FROM READ FILE
    #&VICE VERSA
    


#BASE IMPORTS
from functools import partial
from gettext import translation
import string

from threading import Thread
import threading
import time
from unicodedata import name
from cv2 import sort

from kivymd.app import MDApp
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



Window.size = (200, 400)

class wtf(Screen):
    def __init__(self, **kw):
        super(wtf, self).__init__(**kw)


    def what_now(self, instance):
        print("CLEARED")

    def splash(self, instance, card, **kwargs):
        print("WHATTTT?????", instance, card)
        self.n_card = Button(size=(.4, .4), text=str(card), pos_hint={'x': 0, 'y': .8}, on_press=self.what_now)
        self.ids.new.clear_widgets()
        self.ids.new.add_widget(self.n_card)

    def add_card(self):
        card = Button(size=(.4, .4), text=str("HELLO"), pos_hint={'x': 0, 'y': .2})
        card.bind(on_press=lambda x:self.splash('Ola', card))
        self.ids.new.add_widget(card)

    def what_da(self):
        print(self.ids.what)
        self.add_card()
        self.remove_widget(self.ids.what)


class Game_Page(Screen):
    def __init__(self, **kwargs):
        super(Game_Page, self).__init__(**kwargs)


        self.my_deck = []
        self.opp_deck = []
        self.all_cards = []
        self.table_l = []
        self.table_r = []
        
        self.play_count = 0
        
        self.opp_hand = BoxLayout(
            size_hint=(.5, .4),
            pos_hint={'x': .3, 'y': .6},
            orientation='vertical')
        self.table_left = BoxLayout(size_hint=(.4, .4), pos_hint={'x': .3, 'y': .3})
        self.table_right = BoxLayout(size_hint=(.4, .4), pos_hint={'x': .6, 'y': .3})
        
        
        
        self.my_hand = BoxLayout(size_hint=(.5, .4), pos_hint={'x': .3, 'y': 0})


        self.add_widget(self.opp_hand)
        self.add_widget(self.table_left)
        self.add_widget(self.table_right)
        self.add_widget(self.my_hand)


        self.Widget_List = []

        self.Widget_List.append(self.opp_deck)
        self.Widget_List.append(self.table_left)
        self.Widget_List.append(self.table_right)
        self.Widget_List.append(self.my_deck)
        
        self.FM = File_man()
        

        Clock.schedule_interval(self.fodis, .5)


    def hit_me(self, instance, data):
        print(self.name)
        self.FM.write_file("GAME.txt", str(str(data) + str(self.play_count)), "w")
            
        print("PLAY_COUNT:: ", str(self.play_count))
        self.play_count +=1


    def what_deck(self, what, data):
        
        #WRITE ALL SEND DATA TO FILE...

        self.FM.write_file("GAME.txt", str(str(data) + str(self.play_count)), "w")
            
        print("PLAY_COUNT:: ", str(self.play_count))
        self.play_count +=1
        



    def display_cards(self):
        
        self.opp_hand.clear_widgets()
        self.table_right.clear_widgets()
        self.my_hand.clear_widgets()

        #print("OPP_DECK: ", self.opp_deck)
        #print("MY_DECK:  ", self.my_deck)



        #########################
        for card in self.opp_deck:
            self.oppcard = Button(size_hint=(.1, .4), text=str(card))
            self.opp_hand.add_widget(self.oppcard)
            #print(f'{card} made')


        for card in self.table_r:
            self.myCard = Button(size_hint=(.2, .3), text=str(card))
            self.table_right.add_widget(self.myCard)


        ##########################
        for card in self.my_deck:
            self.mycard = Button(size_hint=(.1, .4), text=str(card), on_press=self.shift)
            self.mycard.bind(on_press=lambda x:self.shift(card))
            self.my_hand.add_widget(self.mycard)
            #print(f'{card} made')


    def shift(self, card):
        #print("SHIFT:: ", card)
        
        #REMOVE CARD FROM MY_HAND -> ADD TO TABLE(RIGHT)        
        if len(str(card)) <= 6:
            self.table_r.append(str(card))
            print("TABLE:: ", self.table_r)
        for i, cards in enumerate(self.my_deck):
            if str(card) in self.my_deck[i]:
                print("FOUND CARD")
                self.my_deck.pop(i)
                #REMOVE FROM TEXT FILE!!!!


    def fodis(self, instance):
        deck = self.FM.read_file("SERVER.txt")
        if "DONE" in deck:
        
            self.FM.write_file("SERVER.txt", "", "w")

        deck_list = str(deck)
        card_set = deck_list.split("@")

        
        for i, card in enumerate(card_set):
            j = i+1
            if "MY" in card_set[i]:
                card_val = str(card_set[j])
                #CHECK IF CARD IS ON TABLE
                if card_val not in self.table_r:
                    if card_val not in self.my_deck:
                        self.my_deck.append(card_set[j])
                

            if "OPP" in card_set[i]:
                if card_set[j] not in self.opp_deck:
                    self.opp_deck.append(card_set[j])
  
        self.display_cards()






class Main_Widget(Screen):
    def __init__(self, **kwargs):
        super(Main_Widget, self).__init__(**kwargs)
        self.G = Game_Page()
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
        print(self.ids.what.text)
        
        
class screen_manager(ScreenManager):
    Main_Widget()
    Game_Page()
    wtf()

class Main(MDApp):
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
#        self.theme_cls.theme
        self.theme_cls.theme_style = "Dark"
        self.FM = File_man()
        sm = ScreenManager()
        return sm
    
    def on_start(self):
        pass

if __name__ == '__main__':
    M = Main()
    M.run() 
