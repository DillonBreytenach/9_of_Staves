#TODO:::  SERVER SIDE COMMS FOR MOVES
######## SERVER SIDE SHUFFLE CARDS< SEND LIST TO GROUPS AT HAND :P



import time
import string
import threading
import kivymd
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window

from functools import partial
from kivy.clock import Clock

from file_handle_C import File_man



Window.size = (300, 560)


class MainWidget(Screen):
    def __init__(self, **kw):
        super(MainWidget, self).__init__(**kw)
        #PLUGIN IMPORTS
        self.FM = File_man()
        
        
        
        
        #DECK POSITION VARIABLES
        #ON_HAND_POSITIONS
        self.deck_pos_1 = [0, 110, False, "USER"]
        self.deck_pos_2 = [30, 110, False, "USER"]
        self.deck_pos_3 = [60, 110, False, "USER"]
        self.deck_pos_4 = [90, 110, False, "USER"]
        self.deck_pos_5 = [120, 110, False, "USER"]
        self.deck_pos_6 = [150, 110, False, "USER"]
        self.deck_pos_7 = [180, 110, False, "USER"]
        self.deck_pos_8 = [210, 110, False, "USER"]

        self.pos_list = [self.deck_pos_1,
                         self.deck_pos_2, 
                         self.deck_pos_3, 
                         self.deck_pos_4,
                         self.deck_pos_5,
                         self.deck_pos_6,
                         self.deck_pos_7,
                         self.deck_pos_8] 



        #OPP_HAND_POS
        #ON_HAND_POSITIONS
        self.opp_pos_1 = [0, 220, False, "USER"]
        self.opp_pos_2 = [30, 220, False, "USER"]
        self.opp_pos_3 = [60, 220, False, "USER"]
        self.opp_pos_4 = [90, 220, False, "USER"]
        self.opp_pos_5 = [120, 220, False, "USER"]
        self.opp_pos_6 = [150, 220, False, "USER"]
        self.opp_pos_7 = [180, 220, False, "USER"]
        self.opp_pos_8 = [210, 220, False, "USER"]

        self.Opp_pos_list = [self.opp_pos_1,
                         self.opp_pos_2, 
                         self.opp_pos_3, 
                         self.opp_pos_4,
                         self.opp_pos_5,
                         self.opp_pos_6,
                         self.opp_pos_7,
                         self.opp_pos_8] 



        #LIST AVAILABLE CARD POSITIONS (TABLE)
        #TODO:::: MAKE TO SIDE OF TABLE FOR GAME PLAY
        self.table_pos_1 = [0.0, 230, False, "USER"]
        self.table_pos_2 = [30.0, 230, False, "USER"]
        self.table_pos_3 = [60.0, 230, False, "USER"]
        self.table_pos_4 = [90.0, 230, False, "USER"]
        self.table_pos_5 = [120.0, 230, False, "USER"]
        self.table_pos_6 = [150.0, 230, False, "USER"]
        self.table_pos_7 = [180.0, 230, False, "USER"]
        self.table_pos_8 = [210.0, 230, False, "USER"]

        self.table_list = [self.table_pos_1,
                         self.table_pos_2, 
                         self.table_pos_3, 
                         self.table_pos_4,
                         self.table_pos_5,
                         self.table_pos_6,
                         self.table_pos_7,
                         self.table_pos_8] 





        #DECK VARIABLES
        self.CardList = []
        self.MyCards = []
        self.OppCards = []
        
        self.ids_l = []

        #**********
        Clock.schedule_interval(self.UPADTE, 1)




    ###ToDo:::: BUILD F_TREES:: 
    ###ToDo:::: MAKE ELIMINATORS ON DRAG AND RELEASE
















    def pos_on_hand(self, card):#DECK ON HAND
        for _ in self.pos_list:
            #print("\n::\n::ON_HAND AVAI", str(_))
            if _[2] != True:
                #print(" >>HAND_SPACE::",str(_))
                _[2] = True
                _[3] = card
                #print("ON_HAND IN_USE", str(_))
                return (_)


    def pos_table(self, card):#DECK ON TABLE
        for _ in self.table_list:
            if card not in _:
            #print("TABLE SPACES >>>", _)
                if _[2] != True:
                    #print(f"MOVING {card} to table :: ->", str(_))
                    _[2] = True
                    _[3] = str(card)
                    return (_)
            




    def at_hand(self, *args):
        print("CARD at PLAY:: ", args[0])

        try:
            posv = self.pos_on_hand(str(args[0]))
            x = posv[0]
            y = posv[1]

            set_x = self.ids[str(args[0])].pos[0]
            set_y = self.ids[str(args[0])].pos[1]
            
            

            #UPDATE SERVER WHICH CARD HAS BEEN TAKEN




            try:
                #print(f"CHECKING DECK>>>", len(self.CardList))
                #print("\n\nCHECKING TABLE SPACE\n\n")
                if set_y == 110.0:
                    pos_t = self.pos_table(str(args[0]))
                    #print("SPACE ON TABLE???", pos_t, "\n\n>>>>>", str(args[0]))
                    self.ids[args[0]].pos[0] = pos_t[0]
                    self.ids[args[0]].pos[1] = pos_t[1]
                    #AFTER MOVING TO TABLE RE_OPEN SPACE ON HAND
                    for card in self.pos_list:
                        if card[3] == args[0]:
                            #print(f"NOW_OPEN  {card} :: {args[0]}")
                            card[3] = "USER"
                            card[2] = False
                    data = str(str(args[0])+"@"+str(self.ids[args[0]].text)+"@TO_TABLE")

            except:
                print("NO_SPACE_ERROR")
                pass             
            
            
            
            
            
            try:
                if set_y < 100.0:
                    data = str(str(args[0])+"@"+str(self.ids[args[0]].text)+"@TO_HAND")
                    #CHECK IF CARD IS ON HAND: IF_SO: CHECK FOR SPACE_ON_HAND -> move there
                    #print("CARD_POS__:X:", set_x,":Y:", set_y)
                    self.ids[str(args[0])].pos[0] = x
                    self.ids[str(args[0])].pos[1] = y

                    set_x = self.ids[str(args[0])].pos[0]
                    set_y = self.ids[str(args[0])].pos[1]
                    set_co_ords = str(set_x+set_y+"@")
                    #print("CARD_POS__:X:", set_x,":Y:", set_y)
                    self.MyCards.append(str(args[0]))


            except:
                print("HANDS ARE FULL")
                pass

#            print("ATTEMPTING TO WRITE DATA")
            self.FM.write_file("GAME.txt", data, "w")

            
        except Exception as e:
            print(e)








    #BACKGROUND PROCESS
    def UPADTE(self, *args):


        #DECK CREATION
        deck = self.FM.read_file("SERVER.txt")
        deck_list = str(deck)
        card_set = deck_list.split("@")

        for key, val in self.ids.items():
            if "DECK" in key:
                print("LAYING DECK:: ", card_set)
            if "TEST" in key:
                if key not in self.ids_l:
                    print("KEY::??",key)
                    self.ids_l.append(key)
        for i, _ in enumerate(card_set):
            try:
                try:
                    j = i+1
                    card = _.translate(str.maketrans('','',string.punctuation))
                    #print(str(card))
                    #print("IDS>>:", str(self.ids_l[i]),"\n")
                    if "DECK" not in card and "OPP" not in card:
                        if len(self.CardList) < 9:    
                            try:
                                
                                if _[4:] not in self.CardList:
                                    self.CardList.append(str(card[4:5]))
                                    print("CARDS_MADE:: ", self.CardList)
                            except Exception as e:
                                print(str(e), "P1")
                        try:
                            val = self.ids_l[i-1]
                            #print("CAR_VAL::", str(val[4:]), "NUM", self.ids[val].text)
                            for k, _ in enumerate(self.ids_l):
                               #print("K: ", k)
                               self.ids[val].text = str(card[4:])
                               #print("\n\nWIDGET:", val, "\nVAL: ",card)

                               #LOOP THROUGH AND ADD ACCORDING TO CARD NUMBER!!!****
                               #self.ids[val].background_normal = "image.png"
                        except Exception as e:
                            print(str(e), "P2")



                    #OPP DECK SEY_UP
                    if "OPP" in card:
                        opp_c = str(card_set[j].translate(str.maketrans('','',string.punctuation)))
                        if "CARD" in opp_c:
                            #print("OPP_CARD", opp_c, "\n>>", )
                            if str(opp_c[4:5]) not in self.OppCards:
                                self.OppCards.append(opp_c[4:5])
                                #print(">OPPS>", self.OppCards)
                        if "SHIFT" in opp_c:
                            opp_cs = str(card_set[j+1].translate(str.maketrans('','',string.punctuation)))
                            print(str(card_set[j-1]), str(card_set[j]), "::", opp_cs)
                            self.Opp_Shift(opp_cs)
                        self.UPDATE_OPP()

                
                
                
                
                
                
                except Exception as e:
                    print(e)

                    


                
            except Exception as e:
                print("NOT THERE", str(e))    

            



    def Opp_Shift(self, card):
        #PROBLEM ->> GETS CALLED IN A LOOP>>>>
        #CHECK ON POS_TABLE TO BE MORE ROBUST...
        print("OPP_SHIFT::",card)
        if card not in self.OppCards:
            pos =  self.pos_table(card)
            self.OppCards.append(card)
    
            print("TABLE_SPACE:: ", pos)
            for i, val in enumerate(self.ids_l):
                if card[4:] in self.ids[val].text:
                    if self.ids[val].pos[1] > 230:
                        print(f"{self.ids[val].text} ->> {pos}")
                        self.ids[val].pos[0] = pos[0]
                        self.ids[val].pos[1] = pos[1]
        



    def pos_on_opp(self, card):#DECK ON HAND
        for _ in self.Opp_pos_list:
            #print("\n:OPP:\n::ON_HAND AVAI", str(_), card)
            
            if card in _:
                print("WHAT??", _, card, '\n')
                return "TAKEN"

            if _[2] != True and card != _[3]:
                #print(" >>HAND_SPACE::",str(_))
                _[2] = True
                _[3] = card
                #print("ON_HAND IN_USE", str(_))
                return (_)







    def UPDATE_OPP(self):
        for i, _ in enumerate(self.OppCards):
            #print("\n---\nOPP_UPDATE", _)
            try:
                for c in self.ids:
                    if self.ids[c].text == str(_):
                        try:

            #                print("\nBOOYA", self.ids[c].text)
            #                print("WoW::")
            #                print(self.ids[c].pos)

                            pos_opp = self.pos_on_opp(_)
             #               print("OPP_POS USING:: ", pos_opp)

                            if pos_opp != "TAKEN":

                                #WRITE FUNC FOR AVAIL SPACE FOR OP HAND                       
                                self.ids[c].pos[0] = pos_opp[0]# self.width*0.7
                                self.ids[c].pos[1] = pos_opp[1]+100

                                print(self.ids[c].pos)

                                print("OPP_SHIFTED??\n\n")
                        except Exception as e:
                            print(e)
                            print("OPP_NOT_SHIFTED")
            except Exception as e:
                print(e)
            #if _ in str(self.ids_l[i].text):
            #    print("BOOm")
            #CHECK CARD NUMBER IN LIST -> MOVE TO OPP HAND POS


class Page(Screen):
    def __init__(self, **kw):
        super(Page, self).__init__(**kw)
        pass



class MyMDApp(MDApp):
    def build(self):
        
        #REMEMBER TO UPDATE ALL FILES ON STARTUP
        
        
        Builder.load_file("main.kv")
        self.screenM = ScreenManager()

        self.MW = MainWidget()
        screen = Screen(name="MainWidget")
        screen.add_widget(self.MW)
        self.screenM.add_widget(screen)


        self.P = Page()
        screen = Screen(name="Page")
        screen.add_widget(self.P)
        self.screenM.add_widget(screen)

        return self.screenM
    
    
if __name__=="__main__":
    M = MyMDApp()
    M.run()