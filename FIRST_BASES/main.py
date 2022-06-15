#TODO:::  SERVER SIDE COMMS FOR MOVES   -- 2/3
######## SERVER SIDE SHUFFLE CARDS< SEND LIST TO GROUPS AT HAND :P//
######## 1) F_TREE
######## 2) ELIMS
######## 3) 
######## 4) SCORES... 'uhhmm..'


from shutil import move
from conns import connections


import string
import threading

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


from kivy.clock import Clock

from file_handle_C import File_man



Window.size = (300, 560)


#@HAND&TESTfourtysix&BOT11@
#@HAND&TESTfourtyfour&BOT9@
#@HAND&TESTfourtytwo&BOT7@
#@HAND&TESTfourty&BOT5@
#@HAND&TESTthirty&BOT7@

#@TABLE&TESTfourtysix&BOT11@
#@TABLE&TESTfourtyfour&BOT9@
#@TABLE&TESTfourtytwo&BOT7@
#@TABLE&TESTfourty&BOT5@
#@TABLE&TESTthirty&BOT7@




class MainWidget(Screen):
    def __init__(self, **kw):
        super(MainWidget, self).__init__(**kw)

        #PLUGIN IMPORTS
        self.FM = File_man()        
        #DECK POSITION VARIABLES
        #ON_HAND_POSITIONS
        self.y_set = 110
        
        self.deck_pos_1 = [0, 110, False, "USER"]
        self.deck_pos_2 = [25, 110, False, "USER"]
        self.deck_pos_3 = [50, 110, False, "USER"]
        self.deck_pos_4 = [75, self.y_set, False, "USER"]
        self.deck_pos_5 = [100, self.y_set, False, "USER"]
        self.deck_pos_6 = [125, self.y_set, False, "USER"]
        self.deck_pos_7 = [150, self.y_set, False, "USER"]
        self.deck_pos_8 = [175, self.y_set, False, "USER"]
        self.deck_pos_9 = [200, self.y_set, False, "USER"]
        self.deck_pos_10 = [225, self.y_set, False, "USER"]
        self.deck_pos_11 = [250, self.y_set, False, "USER"]
        self.deck_pos_12 = [275, self.y_set, False, "USER"]
        self.deck_pos_13 = [300, self.y_set, False, "USER"]

        self.pos_list = [self.deck_pos_1,
                         self.deck_pos_2, 
                         self.deck_pos_3, 
                         self.deck_pos_4,
                         self.deck_pos_5,
                         self.deck_pos_6,
                         self.deck_pos_7,
                         self.deck_pos_8,
                         self.deck_pos_9,
                         self.deck_pos_10,
                         self.deck_pos_11,
                         self.deck_pos_12,
                         self.deck_pos_13] 



        #OPP_HAND_POS
        #ON_HAND_POSITIONS
        #110 + 200
        on_set = 200
        self.opp_pos_1 = [0, self.y_set+on_set, False, "USER"]
        self.opp_pos_2 = [25, self.y_set+on_set, False, "USER"]
        self.opp_pos_3 = [50, self.y_set+on_set, False, "USER"]
        self.opp_pos_4 = [75, self.y_set+on_set, False, "USER"]
        self.opp_pos_5 = [100, self.y_set+on_set, False, "USER"]
        self.opp_pos_6 = [125, self.y_set+on_set, False, "USER"]
        self.opp_pos_7 = [150, self.y_set+on_set, False, "USER"]
        self.opp_pos_8 = [175, self.y_set+on_set, False, "USER"]

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
        #110 + 100
        t_set = 100
        self.table_pos_1 = [0.0, self.y_set+t_set, False, "USER"]
        self.table_pos_2 = [25.0, self.y_set+t_set, False, "USER"]
        self.table_pos_3 = [50.0, self.y_set+t_set, False, "USER"]
        self.table_pos_4 = [75.0, self.y_set+t_set, False, "USER"]
        self.table_pos_5 = [100.0, self.y_set+t_set, False, "USER"]
        self.table_pos_6 = [125.0, self.y_set+t_set, False, "USER"]
        self.table_pos_7 = [150.0, self.y_set+t_set, False, "USER"]
        self.table_pos_8 = [175.0, self.y_set+t_set, False, "USER"]
        self.table_pos_9 = [200.0, self.y_set+t_set, False, "USER"]
        self.table_pos_10 = [225.0, self.y_set+t_set, False, "USER"]
        self.table_pos_11 = [250.0, self.y_set+t_set, False, "USER"]
        self.table_pos_12 = [275.0, self.y_set+t_set, False, "USER"]
        self.table_pos_13 = [300.0, self.y_set+t_set, False, "USER"]
        self.table_pos_14 = [325.0, self.y_set+t_set, False, "USER"]



        self.table_list = [self.table_pos_1,
                         self.table_pos_2, 
                         self.table_pos_3, 
                         self.table_pos_4,
                         self.table_pos_5,
                         self.table_pos_6,
                         self.table_pos_7,
                         self.table_pos_8,
                         self.table_pos_9,
                         self.table_pos_10,
                         self.table_pos_11,
                         self.table_pos_12,
                         self.table_pos_13,
                         self.table_pos_14] 





        #DECK VARIABLES
        self.CardList = []
        self.MyCards = []
        self.OppCards = []
        
        self.ids_l = []


        self.card_at_play = []
        self.group_at_play = []

        #**********
        Clock.schedule_interval(self.UPADTE, 1)




    ###ToDo:::: BUILD F_TREES:: 

    ###ToDo:::: MAKE ELIMINATORS BY CLICKING ON TABLE WIDGETS**



    #REMOVE CARDS TO ELEM DECK
    def kick_it(self, obj, ref):
        #print(obj, ref)
        pass



    #CREATE F_TREES
    def f_tree(self):
        opp_ft = []
        o_ft_len = len(opp_ft)
        opp_fm = []
        o_fm_len = len(opp_fm)
        opp_fb = []
        o_fb_len = len(opp_fb)

        my_ft = []
        my_ft_len = len(my_ft)
        my_fm = []
        my_fm_len = len(my_fm)
        my_fb = []
        my_fb_len = len(my_fb)





        for card in self.OppCards:
            print("OPP_CARD::",card)
            if "TOP" in str(card[1]):
                opp_ft.append(card)
                print("\n\nGOT TOP....")
            if "MID" in str(card[1]):
                opp_fm.append(card)
                print("\n\nGOT MID....")
            if "BOT" in str(card[1]):
                opp_fb.append(card)
                print("\n\nGOT BOT....")
        if o_ft_len == o_fm_len and o_fm_len == o_fb_len:
            if o_ft_len > 0:
                print("\n\n\n______\n   |\n   |\n\n->GOT A TREE??")
        print("____________________")
        print("____________________")

        for card in self.MyCards:
            print("MY__CARD::", card)

            if "TOP" in str(card[1]):
                my_ft.append(card)
                print("\n\nGOT TOP....")
            if "MID" in str(card[1]):
                my_fm.append(card)
                print("\n\nGOT MID....")
            if "BOT" in str(card[1]):
                my_fb.append(card)
                print("\n\nGOT BOT....")
        if my_ft_len == my_fm_len and my_fm_len == my_fb_len:
            if my_ft_len > 0:
                print("\n\n\n______\n   |\n   |\n\n->GOT A TREE??")
                print("TREE??:\n\n", str(my_ft[0]), str(my_fm), str(my_fb))
        print("____________________")
        print("____________________")




    #SHIFTING LISTS MODIFIERS



    #DECK ON (MY)HAND
    def pos_on_hand(self, wid, card):
        
        print("CHECKING MY HAND \n::    **",card, wid )
        #self.f_tree()
        
        for what in self.pos_list:
                print("\nMY_POS_LIST_ITEM:: ", what)
                if what[2] == True:
                    print("USED_SPACE:::  ** ", what)
                    pos_x  = self.ids[str(what[3])].pos[0]
                    pos_y  = self.ids[str(what[3])].pos[1]
                    print(f"POS_X:: {pos_x} >> POS_Y:: {pos_y}\n")
                    if pos_y != 110:
                        what[2] = False
                        what[3] = "USER"
                        print("WIDGET NO LONGER ON HAND:: \n    ::  ", what)
                    else:
                        pass
        
        for what in self.pos_list:
                print("\nMY_POS_LIST_ITEM:: ", what)
                if what[2] == False:
                    print("!BEFORE!\nOPEN_HAND_POS:: ", what)

                    what[2] = True
                    what[3]= wid
                    print("!AFTER!\nOPEN_HAND_POS:: ", what)
                    return (what)

        



    #DECK ON (OPP)HAND
    def pos_on_opp(self, wid, val):
        print("CHECKING OPP HAND")
        for what in self.Opp_pos_list:
                print("\nOPP_POS_LIST_ITEM:: ", what)
                if what[2] == True:
                    print("\n!!\nOBJ_IN_Q:POS: ", str(self.ids[str(what[3])].pos))
                    pos_x  = self.ids[str(what[3])].pos[0]
                    pos_y  = self.ids[str(what[3])].pos[1]
                    print(f"POS_X:: {pos_x} >> POS_Y:: {pos_y}\n")
                    if pos_y != 310:
                        what[2] = False
                        what[3] = "USER"
                        print("WIDGET NO LONGER ON HAND:: \n    ::  ", what)
                    else:
                        pass

        for what in self.Opp_pos_list:
                if what[2] == False:
                    what[2] = True
                    what[3] = wid
                    return (what)




        



    #DECK ON TABLE
    def pos_table(self, wid, card):
        #     SET 
        # my_TABLE_SPACE 
        #     and 
        # opp_TABLE_SPACE
        print("CHECKING OPP HAND")
        for what in self.table_list:
                print("\nOPP_POS_LIST_ITEM:: ", what)
                #for w in what:
                #    print("ITEM_VALS::  ", w)
                if what[2] == True:
                    print("\n!!\nOBJ_IN_Q:POS: ", str(self.ids[str(what[3])].pos))
                    pos_x  = self.ids[str(what[3])].pos[0]
                    pos_y  = self.ids[str(what[3])].pos[1]
                    print(f"POS_X:: {pos_x} >> POS_Y:: {pos_y}\n")
                    if pos_y != 210:
                        what[2] = False
                        what[3] = "USER"
                        print("WIDGET NO LONGER ON HAND:: \n    ::  ", what)
        for what in self.table_list:
                if what[2] == False:
                    what[2] = True
                    what[3] = wid
                    return (what)
        




    def pos_update(self, widget, move):

        try:
            
                print("\n\nMOVE:: ",move, self.ids[widget].pos)
                self.FM.write_file("GAME.txt", move, "w")
                self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
                print("\n\n     *****UPDATED*****\n", move, widget)
                return "DONE"
        except:
            print("POSITION_CHANGE [NOT_UPDATED]")
            pass
            




    def at_hand(self, *args):
        print("CARD at PLAY:: ", args[0])
        widget = str(args[0])
        card_val = str(self.ids[widget].text)
        card_pos = str(self.ids[widget].pos)
        
        print("CARD at PLAY:: ", args[0], card_pos)


        #MOVE (MY)CARD TO (MY)HAND
        #       or
        #MOVE (MY)CARD TO TABLE        

        try:
        
            try:
                #UPDATE MY HAND POS {WID;CARD}
                if self.ids[widget].pos[1] == 10:
                    print("\n************************\nDECK_TO_HAND_->", widget, card_val, "\n")
                    self.MyCards.append([widget, card_val])
                    for c in self.MyCards:
                        print("MY_CARD: ", c)

                    move = "@HAND&"+widget+"&"+card_val+"@"
                    print("\n\nWIDGET_TEXT:: ", str(card_val))
                    print("WIDGET_POS :: ", str(card_pos))

                    posv = self.pos_on_hand(widget, card_val)
                    print("POS_H: ", posv)
                    self.ids[str(args[0])].pos[0] = posv[0]
                    self.ids[str(args[0])].pos[1] = posv[1]

                    self.pos_update(widget, move)
                    return

            except:
                print("CARD_NOT_MOVED_TO_HAND", card_val)

                
            #UPDATE MY CARD MOVED TO TABLE

            try:
                
                if self.ids[widget].pos[1] == 110:
                    
                    print("\n******************************")
                    print("MOVE TO TABLE!!      *********")
                    move = "@TABLE&"+widget+"&"+card_val+"@"

                    self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
                    print("WIDGET_TEXT:: ", str(card_val))
                    print("WIDGET_POS :: ", str(card_pos))

                    posv = self.pos_table(widget, card_val)
                    print("POS_T: ", posv)

                    self.ids[str(args[0])].pos[0] = posv[0]
                    self.ids[str(args[0])].pos[1] = posv[1]
                    
                    self.pos_update(widget, move)

                    print("******************************\n")
                    return
            except:
                print("NO_SPACE_ERROR::[TABLE]")


#_____________________________________________________________
                #ELEMINATOR&**********************
            try:
                if self.ids[widget].pos[1] == 210:
                    
                    print("\n*******************\nBOOMIT\n********************\n")


                    if len(self.card_at_play) < 2:

                        self.card_at_play.append(self.ids[widget])
                        self.ids[widget].disabled=True
                        print(":BOOM_WHAT??",str(args[0]))
                    if len(self.card_at_play) == 2:
                        kill_set = []
                        try:
                            for c in self.card_at_play:
                                self.group_at_play.append(c)
                                kill_set.append(c.text)
                                kill_set.append("&")
                                print("\nMOVING: \n  ", c)
                                c.disbaled = False
                                c.pos[0] = 120.0
                                c.pos[1] = 50.0
#                                #ENCAP

                            
                                data = str("@ELIM&"+str(kill_set)+"@")
#                                #NOW UPDATE SERVER
                                self.FM.write_file("GAME.txt", data, "w")
                            self.card_at_play.clear()
#         
                        except Exception as e:
                            print("ELIM_ERROR::", str(e))
            except Exception as e:
                print("ELEM", str(e))

#_______________________________________________________________________
                #ELEMINATOR&**********************
                

        except Exception as e:
            print(str(e), "AT_HAND()_ERROR")

















    # MAIN BACKGROUND THREAD
    def UPADTE(self, *args):
        #self.f_tree()
        #DECK CREATION

        dck = 0
        cards = []


        for key, val in self.ids.items():
            if "TEST" in key:
                if key not in self.ids_l:
                    self.ids_l.append(key)

        deck = self.FM.read_file("SERVER.txt")

        deck_list = str(deck)
        card_set = deck_list.split("@")


        #UPDATE MOVEMENTS


        for i, fc in enumerate(card_set):
            try:
                card = fc.translate(str.maketrans('','',"@"))
                
                #READ ALL CARD VALUES AND ->> IDS
                if "DECK" in card:
                    print("DECK_SET", card)
                if "CARD" in card:
                    dck += 1
                    cards.append(card)

                #INITIATE GAME
                if "MATCH1" in card:
                    self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'
                    #ENABLE BUTTONS

                if "MATCH2" in card:
                    self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
                    #DISABLE BUTTONS

                if "SET" in card:
                    self.FM.write_file("SERVER.txt", "", "w")
                    print("SERVER.txt -- [CLEARED]")
                    print(self.FM.read_file("SERVER.txt"))




                for i, _ in enumerate(cards):
                    id_val = str(self.ids_l[i])
                    self.ids[id_val].text = str(_[5:])



            except Exception as e:
                print("SETTING_DECK_ERROR", str(e))

            try:
                if "HAND" in fc:
                    self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'

                    move = fc.split("&")
                    mov = move[0]
                    wid = move[1]
                    c = move[2]
                    print("MOVEMENT::: ", mov, c)

                    self.Opp_Shift(mov, wid, c)
                    self.FM.write_file("SERVER.txt", "", "w")
                    print("SERVER.txt -- [CLEARED]")
                    print(self.FM.read_file("SERVER.txt"))

            except Exception as e:
                print("FAILED TO MOVE:: ", str(e))


            try:
                if "TABLE" in fc:
    
    
                    print("\n******************************")
                    print("\n\nDA FUCKN TABLE!!!!!!!!\n\n")

                    self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'

                    move = fc.split("&")
                    mov = move[0]
                    wid = move[1]
                    c = move[2]
                    print("MOVEMENT::: ", mov, c)

                    self.Opp_Shift(mov, wid, c)
                    self.FM.write_file("SERVER.txt", "", "w")
                    print("SERVER.txt -- [CLEARED]\n")

                    print("******************************\n")
            except Exception as e:
                print("FAILED TO MOVE:: ", str(e))


            try:
                if "ELIM" in fc:
                    print("ELIMINATED", fc)
                    elim = fc.split("&")
#                    kill_set =  elim.translate(str.maketrans('','',string.punctuation))

                    for _ in elim:
                        kill = _.translate(str.maketrans('','',' '))
                
                        print("ELIM::::     ", kill)
                        for val in self.ids_l:
                            if self.ids[val].text == str(kill):
                                print("\n!!!!!!\nKILLING::    ",self.ids[val].text)
                                self.ids[val].disabled=True
                                self.ids[val].pos[0] = 120
                                self.ids[val].pos[1] = 450
            except:
                print("ELIM_ERROR")




                
        
            
    #UPDATE OPP_CARD to OPP_HAND POS


    def Opp_Shift(self, action, wid, card):
        #PROBLEM ->> GETS CALLED IN A LOOP>>>>
        #CHECK ON POS_TABLE TO BE MORE ROBUST...
        print("\n---\nOPP_SHIFT::", action, card)

        if card not in self.OppCards:
            self.OppCards.append([wid, card])

        if action == "HAND":
            pos =  self.pos_on_opp(wid, card)
            print("\n\n*******\n        NEW_POS:: ", pos)
        if "TABLE" in action:
            pos =  self.pos_table(wid, card)
            print("TABLE--")
        try:
            self.ids[wid].pos[0] = pos[0]
            self.ids[wid].pos[1] = pos[1]
            #print("MOVED???? ", pos)
        except Exception as e:
            print(str(e), "OPP_SHIFT_ERROR")





class Page(Screen):
    def __init__(self, **kw):
        super(Page, self).__init__(**kw)
        self.FM = File_man()





    def move(self):
        print("[GAME_STARTED]")
        MDApp.get_running_app().root.current ="MainWidget"
        self.FM.write_file("GAME.txt", "START@", "w")


    def ads(self):
        print("PLAYING ADD")
        


    #OFFER_WALL


#class ScreenLayout(PageLayout):
#    pass
class MyMDApp(MDApp):
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
        except:
            print("\n\n!!INIT_CONNECTION_ERROR!!\n\n")

 
 
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

        self.screenM.current="Page"

        return self.screenM
    
    
if __name__=="__main__":
    M = MyMDApp()
    M.run()