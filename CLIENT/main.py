#TODO:::  
######## 1) FIX_ELIM_::UPDATE() 1/2
######## 1) ADS_ 1/3
######## 2) SCORES... 0/3
######## 3) 
######## 4) 


import time

from pexpect import ExceptionPexpect
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
from kivy.uix.image import Image

from kivy.clock import Clock

from file_handle_C import File_man



Window.size = (300, 560)



class MainWidget(Screen):
    def __init__(self, **kw):
        super(MainWidget, self).__init__(**kw)
        #PLUGIN IMPORTS
        self.FM = File_man()        

        #DECK POSITION VARIABLES

        #MY_HAND_POS
        try:
            self.y_set = 110

            self.deck_pos_1 = [0, 110, False, "USER"]
            self.deck_pos_2 = [30, 110, False, "USER"]
            self.deck_pos_3 = [60, 110, False, "USER"]
            self.deck_pos_4 = [90, 110, False, "USER"]
            self.deck_pos_5 = [120, 110, False, "USER"]
            self.deck_pos_6 = [150, 110, False, "USER"]
            self.deck_pos_7 = [180, 110, False, "USER"]
            self.deck_pos_8 = [210, 110, False, "USER"]
            self.deck_pos_9 = [240, 110, False, "USER"]
            self.deck_pos_10 = [0, 90, False, "USER"]
            self.deck_pos_11 = [30, 90, False, "USER"]
            self.deck_pos_12 = [60, 90, False, "USER"]
            self.deck_pos_13 = [90, 90, False, "USER"]
            self.deck_pos_14 = [120, 90, False, "USER"]
            self.deck_pos_15 = [150, 90, False, "USER"]
            self.deck_pos_16 = [180, 90, False, "USER"]
            self.deck_pos_17 = [210, 90, False, "USER"]
            self.deck_pos_18 = [240, 90, False, "USER"]
            self.deck_pos_19 = [270, 90, False, "USER"]
            self.deck_pos_20 = [300, 90, False, "USER"]

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
                             self.deck_pos_13,
                             self.deck_pos_14,
                             self.deck_pos_15,
                             self.deck_pos_16,
                             self.deck_pos_17,
                             self.deck_pos_18,
                             self.deck_pos_19,
                             self.deck_pos_20] 
        except:
            pass

        #OPP_HAND_POS
        try:
            on_set = int(410)
            self.opp_pos_1 = [0, on_set, False, "USER"]
            self.opp_pos_2 = [30, on_set, False, "USER"]
            self.opp_pos_3 = [60, on_set, False, "USER"]
            self.opp_pos_4 = [90, on_set, False, "USER"]
            self.opp_pos_5 = [120, on_set, False, "USER"]
            self.opp_pos_6 = [150, on_set, False, "USER"]
            self.opp_pos_7 = [180, on_set, False, "USER"]
            self.opp_pos_8 = [210, on_set, False, "USER"]
            self.opp_pos_9 = [240, on_set, False, "USER"]
            self.opp_pos_10 = [270, on_set, False, "USER"]
            self.opp_pos_11 = [300, on_set, False, "USER"]
            self.opp_pos_12 = [330, on_set, False, "USER"]
            self.opp_pos_13 = [360, on_set, False, "USER"]
            self.opp_pos_14 = [0, on_set-10, False, "USER"]
            self.opp_pos_15 = [30, on_set-10, False, "USER"]
            self.opp_pos_16 = [60, on_set-10, False, "USER"]
            self.opp_pos_17 = [90, on_set-10, False, "USER"]
            self.opp_pos_18 = [120, on_set-10, False, "USER"]
            self.opp_pos_19 = [150, on_set-10, False, "USER"]
            self.opp_pos_20 = [180, on_set-10, False, "USER"]



            self.Opp_pos_list = [self.opp_pos_1,
                             self.opp_pos_2, 
                             self.opp_pos_3, 
                             self.opp_pos_4,
                             self.opp_pos_5,
                             self.opp_pos_6,
                             self.opp_pos_7,
                             self.opp_pos_8,
                             self.opp_pos_9,
                             self.opp_pos_10,
                             self.opp_pos_11,
                             self.opp_pos_12,
                             self.opp_pos_13,
                             self.opp_pos_14,
                             self.opp_pos_15,
                             self.opp_pos_16,
                             self.opp_pos_17,
                             self.opp_pos_18,
                             self.opp_pos_19,
                             self.opp_pos_20] 
        except:
            pass

        #MY_TABLE_POS
        try:
            self.table_pos_1 = [0, 210, False, "USER"]
            self.table_pos_2 = [30, 210, False, "USER"]
            self.table_pos_3 = [60, 210, False, "USER"]
            self.table_pos_4 = [90, 210, False, "USER"]
            self.table_pos_5 = [120, 210, False, "USER"]
            self.table_pos_6 = [150, 210, False, "USER"]
            self.table_pos_7 = [180, 210, False, "USER"]
            self.table_pos_8 = [210, 210, False, "USER"]
            self.table_pos_9 = [240, 210, False, "USER"]
            self.table_pos_10 = [270, 210, False, "USER"]
            self.table_pos_11 = [300, 210, False, "USER"]
            self.table_pos_12 = [330, 210, False, "USER"]
            self.table_pos_13 = [360, 210, False, "USER"]
            self.table_pos_14 = [390, 210, False, "USER"]


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
        except:
            pass

        #OPP_TABLE_POS
        try:
            t_set = 310
            self.table_opp_1 = [0, t_set, False, "USER"]
            self.table_opp_2 = [30, t_set, False, "USER"]
            self.table_opp_3 = [60, t_set, False, "USER"]
            self.table_opp_4 = [90, t_set, False, "USER"]
            self.table_opp_5 = [120, t_set, False, "USER"]
            self.table_opp_6 = [150, t_set, False, "USER"]
            self.table_opp_7 = [180, t_set, False, "USER"]
            self.table_opp_8 = [210, t_set, False, "USER"]
            self.table_opp_9 = [240, t_set, False, "USER"]
            self.table_opp_10 = [270, t_set, False, "USER"]
            self.table_opp_11 = [300, t_set, False, "USER"]
            self.table_opp_12 = [330, t_set, False, "USER"]
            self.table_opp_13 = [300, t_set, False, "USER"]
            self.table_opp_14 = [325, t_set, False, "USER"]



            self.table_list_opp = [self.table_opp_1,
                             self.table_opp_2, 
                             self.table_opp_3, 
                             self.table_opp_4,
                             self.table_opp_5,
                             self.table_opp_6,
                             self.table_opp_7,
                             self.table_opp_8,
                             self.table_opp_9,
                             self.table_opp_10,
                             self.table_opp_11,
                             self.table_opp_12,
                             self.table_opp_13,
                             self.table_opp_14] 
        except:
            pass    




        #POINT_SYSTEMS_VARIABLES
        self.turn = False
        self.my_point = 0
        self.opp_point = 0
        self.round_out = 0
        self.winner = ""
        
        #ELIM_SET
        self.elim_set = []
        self.elim_count = 0

        #DECK_VARIABLES
        self.CardList = []
        self.MyCards = []
        self.OppCards = []
        self.ids_l = []



        #SPECIAL_PRIVILEGE_CARDS
        self.my_sp_cards = []
        self.sp1_active = False
        self.sp2_active = False
        self.sp3_active = False



        #ELIM_VARIABLES
        self.card_at_play = []
        self.group_at_play = []



        #CHECK_LIST_VARIABLES
        self.on_Hand = []
        self.on_Table = []
        self.on_Hand_Opp = []
        self.on_Table_Opp = []



        #FRUITLESS_TREE_VARIABLES
        self.ftr_c_s = []
        self.ftrc_in_use = []
        self.ftr_c_opp = []
        self.ftrc_in_use_opp = []
        self.ftr_c = 0
        self.ftr_c_op = 0


        #DATA_TRANSFER_VARIABLE
        self.move = ""

        #**********
        #UPDATER
        Clock.schedule_interval(self.UPADTE, 1)


    def score_track(self):
        try:
            for _ in self.ids_l:
                current_pos = _
        except Exception as e:
            print("SCORE_TRACKING_ERROR:: ", str(e))        

    #CREATE F_TREE OPP(s)
    def opp_force_tree(self, old_cards, new_card):
        self.check_all()
        #print("OLD:: ", old_cards)
        #print("NEW:: ", new_card)
        print("OPP_FTR\n      |\n     |\n     |\n_________")
        #CLEAR OUT ALL T_M_Bs
        for widget in old_cards:
            self.ids[widget].pos[0] = 300
            try:
                if widget in self.on_Hand_Opp:
                    self.on_Hand_Opp.remove(widget)
                else:
                    print("WHERE IS  ", widget, "?")

            except Exception as e:
                print("OPP_FTREE_ERROR:::",str(e))
            print("MOVED OLD CARD: ", str(widget))


        try:
            pos_xy = list(self.pos_on_opp(str(new_card)))
            if pos_xy != None:
                if new_card not in self.ftrc_in_use_opp:
                    self.ftrc_in_use_opp.append(new_card)
                else:
                    print(f"\n\n!!{new_card} already in use\n\n!")
                if new_card not in self.OppCards:
                    self.OppCards.append(new_card)
                print("!!\nOPP_F_FTRE:pos:",str(pos_xy)) 
                self.ids[str(new_card)].pos[0] = pos_xy[0]
                self.ids[str(new_card)].pos[1] = pos_xy[1]
                self.ids[str(new_card)].disabled = False

                #DOUBLE CHECK
                try:
                    x_ = self.ids[str(new_card)].pos[0]
                    y_ = self.ids[str(new_card)].pos[1]
                    print("CHECKING_OPP_FTREE::", x_, "::", y_, "   <<\n")
                    for ft_s in self.ftrc_in_use_opp:
                        print(f'{ft_s} in: self.ftrc_in_use_opp........')
                except Exception as e:
                    print(f'CHECKING_OPP_FTREE_LIST::ERROR', str(e))

        except Exception as e:
            print("OPP_FORCE_F_TREE:::", str(e))

    #CREATE F_TREES(mine)
    def f_tree(self):
        my_ft = []
        my_ft_len = len(my_ft)
        my_fm = []
        my_fm_len = len(my_fm)
        my_fb = []
        my_fb_len = len(my_fb)


        for card in self.MyCards:
            #print("MY__CARD::", card)
            cah_pos = self.ids[card].pos
            cah = str(self.ids[card].background_normal) 
            self.check_all()
            #PRELIM
            if cah_pos[1] != 110 and cah_pos[1] != 90:
                #print("PRELIM_CHECKS::\n")
                #REMOVE FROM ALL LIST...
                if cah in my_ft:
                    my_ft.remove(cah)
                    #print(f"{cah} Removed")
                if cah in my_fm:
                    my_fm.remove(cah)      
                    #print(f"{cah} Removed")      
                if cah in my_fb:
                    my_fb.remove(cah)
                    #print(f"{cah} Removed")


            if "FTR_T" in cah and "Opp" not in cah:
                my_ft.append(card)
                #print("\n\nGOT TOP....", card, cah)
            if "FTR_M" in cah and "Opp" not in cah:
                my_fm.append(card)
                #print("\n\nGOT MID....", card, cah)
            if "FTR_B" in cah and "Opp" not in cah:
                my_fb.append(card)
                #print("\n\nGOT BOT....", card, cah)
            my_ft_len = len(my_ft)
            my_fm_len = len(my_fm)
            my_fb_len = len(my_fb)
        #CHECK IF T_M_B HAS OCCURED 
        if my_ft_len > self.ftr_c:
            if my_fm_len > self.ftr_c:
                if my_fb_len > self.ftr_c:
                    print("\n*******************\n\n______\n   |\n   |\n\n->GOT A TREE??")
                    print("TREE??:\n::my_ft[]::my_fm[]::my_fb[]::\n", str(my_ft), str(my_fm), str(my_fb))

                    #MOVE ALL T_M_Bs to side.. replace with 1 FTR_C
                    self.ids[my_ft[self.ftr_c]].pos[0] = 300
                    self.ids[my_ft[self.ftr_c]].pos[1] = 10
                    wid1 = str(my_ft[self.ftr_c])
                    if wid1 in self.on_Hand:
                        self.on_Hand.remove(wid1)
                    elif wid1 in self.MyCards:
                        self.MyCards.remove(wid1)
                    else:
                        print("PROBLEM:: ", wid1, self.on_Hand)

                    self.ids[my_fm[self.ftr_c]].pos[0] = 300
                    self.ids[my_fm[self.ftr_c]].pos[1] = 10
                    wid2 = str(my_fm[self.ftr_c])
                    if wid2 in self.on_Hand:
                        self.on_Hand.remove(wid2)
                    elif wid2 in self.MyCards:
                        self.MyCards.remove(wid2)
                    else:
                        print("PROBLEM:: ", wid2, self.on_Hand)

                    self.ids[my_fb[self.ftr_c]].pos[0] = 300
                    self.ids[my_fb[self.ftr_c]].pos[1] = 10
                    wid3 = str(my_fb[self.ftr_c])
                    if wid3 in self.on_Hand:
                        self.on_Hand.remove(wid3)
                    elif wid3 in self.MyCards:
                        self.MyCards.remove(wid3)
                    else:
                        print("PROBLEM:: ", wid3, self.on_Hand)

                    try:
                        
                        ftr = str(self.ftr_c_s[self.ftr_c])
                        if ftr not in self.ftrc_in_use:
                            self.ftrc_in_use.append(ftr)
                        #CHECK LIST::
                        for f_card in self.ftrc_in_use:
                            print("FTR_SET:: ", f_card)


                        self.MyCards.append(ftr)
                        self.on_Hand.append(ftr)

                        op_pos = self.pos_on_hand(ftr)
                        if op_pos != None:
                            print("MAKING FTR_C", op_pos)
                            self.ids[ftr].pos[0] = op_pos[0]
                            self.ids[ftr].pos[1] = op_pos[1]

                        print("\n*****************\n                FTR:::::::", ftr)
                        

                        if "Opp" in ftr:
                            print("WTF", ftr)
                            ftr = ftr[:-3]
                            print("WTF", ftr)




                        #FOLD FOR SWITCHING T_M_B for FTR_C
                        
                        data = "HAND#FOLD&"+ftr+"Opp&"+str(my_ft[self.ftr_c])+"&"+str(my_fm[self.ftr_c])+"&"+str(my_fb[self.ftr_c])
                        #UPDATE THE SERVER :6
                        self.FM.write_file("GAME.txt", data, "w")

                        self.ftr_c +=1
                    except Exception as e:
                        print(e)

 #_#SHIFTING LISTS MODIFIERS
    #DECK ON (MY)HAND
    def pos_on_hand(self, wid):
        for what in self.pos_list:
            if wid in what:
                print("ALREADY_HERE", wid,"::", what)
            if what[2] == False:
                what[2] = True
                what[3]= wid
                if wid not in self.on_Hand:
                   self.on_Hand.append(str(wid))
                return (what)

    #DECK ON (OPP)HAND
    def pos_on_opp(self, wid):
        for what in self.Opp_pos_list:
            if what[2] == False:
                what[2] = True
                what[3] = wid
                print("SPACE ON OPP HAND::", what)
                if wid not in self.on_Hand_Opp:
                    self.on_Hand_Opp.append(str(wid))
                    print("on_HAND_OPP:: ", wid)
                return (what)
    
    #DECK ON TABLE
    def pos_table(self, wid):
        #     SET 
        # my_TABLE_SPACE 
        self.on_Table.append(str(wid))
        if str(wid) in self.on_Hand:
            self.on_Hand.remove(str(wid))
            print(f"!!\n{wid} move from 'self.on_Hand' to 'self.on_Table'\n")

        for what in self.table_list:
            if what[2] == True:
                pos_y  = self.ids[str(what[3])].pos[1]
                if pos_y != 210:
                    what[2] = False
                    what[3] = "USER"
                    #print("WIDGET NO LONGER ON TABLE:: \n    ::  ", what)
        for what in self.table_list:

            if what[2] == False:
                what[2] = True
                what[3] = wid
                return (what)

    #DECK ON TABLE (OPP)
    def pos_table_opp(self, wid):
        #     SET 
        # opp_TABLE_SPACE
        
        if str(wid) in self.on_Hand_Opp:
            self.on_Hand_Opp.remove(str(wid))
            self.on_Table_Opp.append(str(wid))
        else:
            print("!!!!\n\n!!!\n:POS_TABLE_OPP:\n!!BIG_PROBLEM TO COME, ", str(wid))
        po_y  = self.ids[wid].pos[1]
        print("CHECKING TABLE SPACE (OPP)", wid, po_y)
        for what in self.table_list_opp:
            if what[2] == False:
                what[2] = True
                what[3] = wid
                print("WHAT:TABLE_LIST:->:",what)
                return (what)

    #TODO... maybe
    def settings(self):
        print("SETTINGS??")

    #CHECK SP_CARDS
    def check_sp(self, wid):
        print("TESTING SP_CARDS:: ", wid)
        if "one" in wid and self.sp1_active == True:
            self.at_hand(wid)
            print("ACTIVE")
        if "two" in wid and self.sp2_active == True:
            self.at_hand(wid)
            print("ACTIVE")
        if "three" in wid and self.sp3_active == True:
            self.at_hand(wid)
            print("ACTIVE")

    #SHIFT EACH CARD TO MOST LEFT POSITION
    def check_all(self, **args):
        #print("^^^^^^^^^^^^^^^^^^\nCHECK_ALL\n")

        #COPY LIST AT HAND::
        #   #CLEAR LIST: -> set_all: False, "USER"
        #   #SET_NEW_POS(s)


        #CHECK MY_HAND_POS(s)
        try:
            pos_y = ""
            #SHIFT USED CARDS TO THE LEFT FUNCTION REQUIRED HERE
            try:
                #print("MY_HAND::/")
                #RESET ALL VARIABLES IN LIST(POS)
                for clr in self.pos_list:
                    clr[2] = False
                    clr[3] = "USER"
            except Exception as e:
                print("CLEARING:POS_LIST:ERROR: ", str(e))
            
            try:
                #ITERATE THROUGH LIST(BACK_UP)
                for i, new_c in enumerate(self.on_Hand):

                    #
                    #pos_ = self.ids[str(new_c)].pos
                    
                    #GET NEW POS()
                    new_pos = self.pos_list[i]

                    try:
                        #UPDATE LIST(POS)
                        self.pos_list[i][2] = True
                        self.pos_list[i][3] = str(new_c)
                    
                        what = []
                        what = self.ids[str(new_c)].pos
                    except Exception as e:
                        print("SETTING:VALS:POS_LIST::ERROR", str(e))
                    try:
                        #UPDATE WIDGET POS
                        self.ids[str(new_c)].pos[0] = str(new_pos[0])
                        self.ids[str(new_c)].pos[1] = str(new_pos[1])

                    except Exception as e:
                        print(f"SHIFTING:{new_c}:ERROR:: ", str(e))
            except Exception as e:
                print(e)
                print("^^RESETTING:MY_HAND:ERROR:: \n")


        except Exception as e:
            print("FAILED TO RESET MY HAND:: ", str(e))





        # my_TABLE_SPACE
        try:
            #print("CHECKING TABLE SPACE (MY)")
            for what in self.table_list:
                if what[2] == True:
                    pos_y  = self.ids[str(what[3])].pos[1]
                    if pos_y != 210:
                        what[2] = False
                        what[3] = "USER"
        except Exception as e:
            print("CHECK_TABLE_SPACE:MINE:ERROR:: ", str(e))




        try:
            #print("$$$")
            #CHECK OPP TABLE POS(s)
            try:
                #print("CHECKING TABLE SPACE (OPP)")
                #CLEAR LIST(POS)
                for clr_opp in self.table_list_opp:

                    clr_opp[2] = False
                    clr_opp[3] = "USER"

            except Exception as e:
                print("CHECK_TABLE(OPP)::ERROR", str(e))

            try:
                #ITERATE THROUGH LIST(BACK_UP)
                for j, new_op in enumerate(self.on_Table_Opp):
                    pos_ = self.ids[str(new_op)].pos
                    new_pos = self.table_list_opp[j]
                    #print("$$$POS_:OPP:TABLE", new_op, pos_)
                    try:
                        self.table_list_opp[j][2] = True
                        self.table_list_opp[j][3] = str(new_op)
                        what = []
                        what = self.ids[str(new_op)].pos
                    except Exception as e:
                        print("SETTING:VALS:POS_LIST:OPP:ERROR", str(e))
                    try:
                        self.ids[str(new_op)].pos[0] = str(new_pos[0])
                        self.ids[str(new_op)].pos[1] = str(new_pos[1])

                        #che_po= self.ids[str(new_op)].pos
                        #print("OPP_TABLE_TABBING:: ", che_po)
                    except Exception as e:
                        print(f"SHIFTING:{new_op}:ERROR:: ", str(e))
            except Exception as e:
                    print(e)
                    print("^^RESETTING:OPP_HAND:ERROR:: \n")
        except Exception as e:
            print("WHAT WENT WORNG::?", str(e))




        for what in self.table_list_opp:
            if what[2] == True:
                pos_y  = self.ids[str(what[3])].pos[1]
                if pos_y != 310:
                    self.on_Table_Opp.remove(str(what[3]))
                    what[2] = False
                    what[3] = "USER"




        #CHECK OPP HAND POS(s)
        for what in self.Opp_pos_list:
            if what[2] == True:
                pos_y  = self.ids[str(what[3])].pos[1]
                if pos_y != 410 and pos_y != 400:
                    #self.on_Hand_Opp.remove(str(what[3]))
                    what[2] = False
                    what[3] = "USER"
                    

        #CHECK MY_HAND_POS(s)
        try:
            card_count = 0
            pos_x = ""
            pos_y = ""
            pos_ = []
            #print("CHECKING_MY_HAND::POS_LIST\n******")

            #SHIFT USED CARDS TO THE LEFT FUNCTION REQUIRED HERE
            try:
                #print("!!!\nCLEARING POS_LIST::\n**")
                for clr in self.Opp_pos_list:
                    clr[2] = False
                    clr[3] = "USER"
                #print("CLEARED:: \n**")
            except Exception as e:
                print("CLEARING:POS_LIST:ERROR: ", str(e))
            
            try:
                for i, new_c in enumerate(self.on_Hand_Opp):


                    pos_x  = str(self.ids[str(new_c)].pos[0])
                    pos_y  = str(self.ids[str(new_c)].pos[1])
                 #   print("AT_:X_", pos_x)
                  #  print("AT_:Y_:", pos_y)



                    new_pos = self.Opp_pos_list[i]

                    try:
                        self.Opp_pos_list[i][2] = True
                        self.Opp_pos_list[i][3] = str(new_c)
                    
                    except Exception as e:
                        print("SETTING:VALS:POS_LIST::ERROR", str(e))
                    try:
                        self.ids[str(new_c)].pos[0] = str(new_pos[0])
                        self.ids[str(new_c)].pos[1] = str(new_pos[1])

                    except Exception as e:
                        print(f"SHIFTING:{new_c}:ERROR:: ", str(e))
            except Exception as e:
                print(e)
                print("^^RESETTING:MY_HAND:ERROR:: \n")
        except Exception as e:
            print("FAILED TO RESET MY HAND:: ", str(e))








        return

    #DATA_UPDATER_::->SERVER
    def pos_update(self, move):
        print("\n***********************************************\nUPDATING\n")
        print("MOVE_COUNT_::", str(self.round_out))
        self.round_out+=1
        
        
        
        
        
        

        try:
            self.FM.write_file("GAME.txt", move, "w")
            self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
            self.turn = False
            print("\n\n     *****UPDATED*****\n\n*************************************\n", move)
            return "DONE"
        except:
            print("POSITION_CHANGE [NOT_UPDATED]")
            pass


    #WHEN CLICKING ON A CARD
    def at_hand(self, *args):
        ks = []
        #print(":wtf:", self.elim_set)
        
        #prod
        widget = str(args[0])
        card = self.ids[widget].background_normal
        x = str(self.ids[widget].pos[0])
        y = str(self.ids[widget].pos[1])
        print("CARD at PLAY:: ",card, widget, x, y)

        #turnBasingLock
        if self.turn == False:
            print("NOT_YOUR_TURN")
            return

        try:
            if int(y) >= 399.0:
                print("NOT_YOURs")
                return
        except:
            print("\n\n\nTHIS IS ANNOYING NOW\n\n!!")
            pass



        try:

                #ELEMINATOR&**********************
            try:
                if self.ids[widget].pos[1] == 310 or self.ids[widget].pos[1] == 210:
                    
                    print("\n*******************\nBOOMIT\n********************\n")
                    try:

                        if len(self.card_at_play) < 2:
                            if widget not in self.card_at_play:
                                self.card_at_play.append(widget)
#                                self.ids[widget].disabled=True
                                print(":BOOM_WHAT??",self.card_at_play)

                    except Exception as e:
                        print(e)
                    
                    if len(self.card_at_play) == 2:
                        kill_set = []
                        try:
                            for i, c in enumerate(self.card_at_play):
                                if c in self.on_Table:
                                    self.on_Table.remove(c)
                                if c in self.on_Table_Opp:
                                    self.on_Table_Opp.remove(c)
                                try:
                                    self.ids[c].pos[0] = 250
                                    self.ids[c].pos[1] = 10
                                    new_post = self.ids[c].pos
                                    print("ELIM_SHIFT:ON_HAND()::: ", str(c), "::", str(new_post))
                                except Exception as e:
                                    print("ELIM_SHIFT::ERROR:ON_HAND()::", str(e))
#                                self.ids[c].disbaled = True
                                #SWAP OPPs
                                if "FTR" in c:
                                    print("ELIMINATING AN FTR_::", c)
                                    if "Opp" in c:
                                        print("Opp found",c, "::",i)
                                        c = c[:-3]
                                        print("SWAPPING OPP:: ", c)
                                        pass
                                    else:
                                        c += "Opp"
                                        print("SWAPPING OPP:: ", c)
                                self.group_at_play.append(c)
                                kill_set.append(c)
                                kill_set.append("&")
                                print("\nMOVING: \n  ", c)

                                        
                        except Exception as e:
                            print("ELIM_ERROR:OPP:", str(e))     
                        #ADD CARDS TO ELIM_SET
                        try:
                            ks = [self.elim_count, str(self.card_at_play[0]), str(self.card_at_play[1]) ]
                            self.elim_count+=1
                            print("#*#*#*#::\n::ELIMINATED CARDS:KS: ", ks, "\n\n#*#*#*#*#\n",self.elim_set)
                            self.elim_set.append(ks)
                            self.group_at_play.clear()
                            for _ in self.elim_set:
                                print(f"ELIM_SET::", str(_))
                        except Exception as e:
                            print("WTF_ELIM:: ", str(e))
                        print("ELIM POINT TO YOU :)")
                        self.my_point += 1
                        print(":ME:  ", self.my_point, "\n:OPP:  ", self.opp_point)
                        self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
                        self.turn = False 
                        self.card_at_play.clear()
                        #NOW UPDATE SERVER

                        data = str("@ELIM&"+str(kill_set)+"&"+str(self.my_point)+"@")
                        self.pos_update(data)
                        return


            except Exception as e:
                print("ELEM", str(e))

#_______________________________________________________________________
                #ELEMINATOR&**********************
            

            try:
                if self.ids[widget].pos[1] == 110 or self.ids[widget].pos[1] == 90:
                    
                    card = self.ids[widget].background_normal
                    print("CARD:: ",card)

                    if str(widget) in self.on_Table:
                        self.on_Table.remove(widget)

                    if "FTR_T" in card or "FTR_M" in card or "FTR_B" in card:
                        print("THAT CARD IS NOT PLAYABLE", card, widget)
                        return


                    print("\n******************************")
                    print("MOVE TO TABLE!!      *********")

                    posv = self.pos_table(widget)
                    print("POS_T: ", posv, ">>:", widget)

                    print("CHECK_ALL:to_Table: ")


                    self.ids[str(args[0])].pos[0] = posv[0]
                    self.ids[str(args[0])].pos[1] = posv[1]

                    if "FTR" in str(widget):
                        self.move = "@TABLE&"+widget+"Opp"
                        widget = widget+"Opp"
                        print("\n\nto_TABLE:move:widget: ",self.move, widget)
                    else:
                        self.move = "@TABLE&"+widget
                        print("\n\nto_TABLE:move:widget: ",self.move)

                    self.pos_update(self.move)
                    self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
                    self.turn = False
                    
                    print("PROBLEM_HERE??")


                    print("******************************\n")
                    return
            except Exception as e:
                print("SPACE_ERROR::[TABLE]", str(e))

            try:
                #UPDATE MY HAND POS {WID;CARD}
                if self.ids[widget].pos[1] == 10:
                    print("\n************************\nDECK_TO_HAND_->", widget,"\n")
                    if widget not in self.MyCards and "Opp" not in str(widget):
                        self.MyCards.append(widget)
                    print("LINE :: 669")
                    self.move = "@HAND&"+widget
                    print("WIDGET_POS :: ", x, y)
                    posv = self.pos_on_hand(widget)

                    print("POS_H: ", posv)
                    self.ids[widget].pos[0] = posv[0]
                    self.ids[widget].pos[1] = posv[1]

                    self.pos_update(self.move)
                    return
            except Exception as e:
                print("CARD_NOT_MOVED_TO_HAND", widget, str(e))
            #UPDATE MY CARD MOVED TO TABLE
            try:
                self.FM.write_file("GAME.txt", "", "w")
            except Exception as e:
                print("CLEARING GAME.txt ERROR: ", str(e))
#____________________________________    
        except Exception as e:
            print(str(e), "AT_HAND()_ERROR")

#______________________________________________________________
#########    AUTO  UPDATE FUNCTIONALITY  ################

    # MAIN BACKGROUND THREAD
    def UPADTE(self, *args):
        
        #PRELIM_CHECKS
        self.score_track()
        self.check_all()
        self.f_tree()

        #DECK CREATION
        #IMPLIMENT SP_CARDS READING ADS_BANK.txt
        sp_cards = str(self.FM.read_file("ADS_BANK.txt"))
        #print("SP_CARDS::: ", sp_cards)
        spc = sp_cards.translate(str.maketrans('','',"@"))
        self.ids.POINTS.text="MY_POINTS:"+str(self.my_point)+"\nOPP_POINTS:"+str(self.opp_point)

        try:
            if "ONE" in sp_cards or "ONE" in spc:
                self.ids['EXTRAthree'].background_normal = "ASSETS/JOKER.jpg"
                self.ids['EXTRAthree'].disbaled=False
                self.sp1_active = True
                print("SP_CARD_1: ACTIVE")

            if "TWO" in sp_cards:
                self.ids['EXTRAtwo'].background_normal = "ASSETS/JOKER.jpg"
                self.ids['EXTRAtwo'].disabled=False
                self.sp2_active = True
                print("SP_CARD_2: ACTIVE")

            if "THREE" in sp_cards:
                self.ids['EXTRAone'].background_normal = "ASSETS/JOKER.jpg"
                self.ids['EXTRAone'].disabled=False
                self.sp3_active = True
                print("SP_CARD_3: ACTIVE")

            try:
                source = 'ASSETS/JOKER.jpg'
                self.ids['EXTRAthree'].background_normal = source
            except Exception as e:
                print("IMAGE_MOUNTING_ERROR::: ", str(e))  
        except Exception as e:
            print("SP_CARDS_SETUP::EROR", str(e))


        #DECK CREATION
        try:
            dck = 0
            cards = []
            for key, val in self.ids.items():
                if "TEST" in str(key):
                    if key not in self.ids_l:
                        self.ids_l.append(key)
                        print("LISTING:TEST: ", key, "::TEST_#")
                if "FTR" in str(key):
                    if "Opp" not in str(key):
                        if key not in self.ftr_c_s:
                            print("LISTING:FTR:MINE: ", key, "::FTR_C_S")
                            self.ftr_c_s.append(key)
                    if "Opp" in str(key):
                        if key not in self.ftr_c_opp:
                            print("LISTING:FTR:_OPP: ", key, "::FTR_C_OPP")
                            self.ftr_c_opp.append(key)
        except Exception as e:
            print("DECK_CREATAION ERROR:: ", str(e))

        deck = self.FM.read_file("SERVER.txt")
        deck_list = str(deck)
        card_set = deck_list.split("@")

        if len(card_set) > 2:
            
            print("***************************\nINCOMING UPDATE\n******************************")
        else:
            return

        #DECK 
        for i, fc in enumerate(card_set):
            #SET_UP
            try:
                card = fc.translate(str.maketrans('','',"@"))

                #READ ALL CARD VALUES AND ->> IDS
                if "CARD" in card:
                    dck += 1
                    cards.append(card)

                #INITIATE GAME
                if "MATCH1" in card:
                    self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'
                    self.turn = True

                    #ENABLE BUTTONS

                if "MATCH2" in card:
                    self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
                    self.turn = False

                    #DISABLE BUTTONS

                if "SET" in card:
                    self.FM.write_file("SERVER.txt", "", "w")

                for i, _ in enumerate(cards):
                    id_val = str(self.ids_l[i])
                    self.ids[id_val].text = ""
                    if "TOP" in str(_):
                        #print("TOP CARD: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/FTR_T.jpg'
                    if "MID" in str(_):
                        #print("MID CARD: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/FTR_M.jpg'
                    if "BOT" in str(_):
                        #print("BOT CARD: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/FTR_B.jpg'
                    if "JOKER" in str(_):
                        #print("JOKER_CARD: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/FTR_C.jpg'
                    if "RUNE_YAH_RAH" in str(_):
                        #print("RUNE_CARD: YAH_RAH: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/RUNE_YAH_RAH.jpg'
                    if "RUNE_RAH_GOOL" in str(_):
                        #print("RUNE_CARD: HAR_GOOL: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/RUNE_HAR_GOOL.jpg'
                    if "RUNE_ALL_GIZ" in str(_):
                        #print("RUNE_CARD: ALL_GIZ: ", id_val)
                        self.ids[id_val].background_normal='ASSETS/RUNE_ALL_GIZ.jpg'
            except Exception as e:
                print("SETTING_DECK_ERROR", str(e))



            #UPDATE MOVEMENTS (HAND_)
            try:                
                if "HAND" in fc:
                    if "FOLD" in fc:
                        print("\n\nOpp_Made_FTREE__: msg-> ", fc)
                        list_form = fc.split("&")
                        print("msg.split('&')  ->  ", list_form)
                        new_ = list_form[1]
                        old_ = [str(list_form[2]),str(list_form[3]),str(list_form[4])]
                        self.opp_force_tree(old_, new_)
                        self.FM.write_file("SERVER.txt", "", "w")
                    else:
                        print("UPDATE_:: ", fc)
                        self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'
                        self.turn = True
                        move = fc.split("&")
                        mov = move[0]
                        wid = move[1]
                        self.Opp_Shift(mov, wid)
                        self.FM.write_file("SERVER.txt", "", "w")
                        print("***********************")
                        print("OPP_SHIFT_COMPLETE::\n")
            except Exception as e:
                print("FAILED TO MOVE:HAND: ", str(e))

            #UPDATE MOVEMENTS (TABLE_)
            try:
                if "TABLE" in fc:
                    print("\n******************************\n       TABLE")

                    self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'
                    self.turn = True

                    move = fc.split("&")
                    mov = move[0]
                    wid = move[1]
                    self.Opp_Shift(mov, wid)
                    self.FM.write_file("SERVER.txt", "", "w")
                    print("***********************")
                    print("OPP_SHIFT_COMPLETE::\n")
            except Exception as e:
                print("FAILED TO MOVE:TABLE: ", str(e))

            #UPDATE MOVEMENTS (ELIM_)
            try:
                if "ELIM" in fc:
                    for _ in self.elim_set:
                        print("ELIM'D_CARD::", str(_))
                    elim = fc.split("&")
                    print("ELIM???????\nSPLIT(&):: ", str(elim))
                    try:
                        wid_01 = str(elim[1])
                        wid_02 = str(elim[2])
                        
                        wid_1 = wid_01.translate(str.maketrans('','',' '))
                        wid_2 = wid_02.translate(str.maketrans('','',' '))
                                                
                        print(f"WID_1:{wid_1}\nWID_2:{wid_2}")
                        #REMOVE WIDS -> off all Lists
                        try:

                            try:
                                if wid_1 in self.on_Table:
                                    self.on_Table.remove(wid_1)
                                if wid_2 in self.on_Table:
                                    self.on_Table.remove(wid_2)
                            except Exception as e:
                                print("ELIM:myTable_REM:ERROR", str(e))

                            try:
                                if wid_1 in self.on_Table_Opp:
                                    self.on_Table_Opp.remove(wid_1)
                                if wid_2 in self.on_Table_Opp:
                                    self.on_Table_Opp.remove(wid_2)
                            except Exception as e:
                                print("ELIM:OppTable_REM:ERROR", str(e))


                        except Exception as e:
                            print("ELIM_LIST_REM::ERROR", str(e))
                        #REMOVE WIDS -> off table
                        try:                            
                            self.ids[wid_1].pos[0] = 250
                            self.ids[wid_1].pos[1] = 411
                            

                            
                            self.ids[wid_2].pos[0] = 250
                            self.ids[wid_2].pos[1] = 411

                            wid_1_test = self.ids[wid_1].pos
                            
                            wid_2_test = self.ids[wid_2].pos
                            
                            print(f"$%$% NEW_POS    \n{wid_1}::{str(wid_1_test)}\n{wid_2}::{str(wid_2_test)}")

                        except Exception as e:
                            print("ELIM_SHIFT::ERROR", str(e))              
                    except Exception as e:
                        print("ELIM:::ERROR", str(e))





                    self.ids.OPP.text='ACTIVE'+'\nYOUR_TURN'
                    self.turn = True
                    self.opp_point = int(elim[4])
                    self.ids.POINTS.text="MY_POINTS:"+str(self.my_point)+"\nOPP_POINTS:"+str(self.opp_point)
                    self.FM.write_file("SERVER.txt", "", "w")

                    print("***********************")
                    print("ELIM_COMPLETE::\n")
                    return
            except Exception as e:
                print("ELIM_ERROR_::UPDATE():", str(e))

    #UPDATE OPP_CARD to OPP_HAND POS
    def Opp_Shift(self, action, wid):
        print("OPP_SHIFT:: ", action, wid)
        #PROBLEM ->> GETS CALLED IN A LOOP>>>>
        #CHECK ON POS_TABLE TO BE MORE ROBUST...
        try:
            if "EXTRA" in str(wid):
                if "Opp" not in str(wid):
                    wid += "Opp"
                elif "Opp" in str(wid):
                    wid = wid[:-3]
        except:
            pass

        try:
            pos = []
            if wid not in self.OppCards:
                self.OppCards.append(wid)
            if "FOLD" in action:
                mpos =  self.pos_on_opp(wid)
            if action == "HAND":
                mpos =  self.pos_on_opp(wid)
            if "TABLE" in action:
                mpos =  self.pos_table_opp(wid)
            print("OPP_SHIFT:->:", wid, "::", pos, ":->:", mpos)
            self.ids[wid].pos[0] = mpos[0]
            self.ids[wid].pos[1] = mpos[1]
            return
        except Exception as e:
            print(str(e), "OPP_SHIFT_ERROR")


class Score(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def score(self):
        pass

class AdsBank(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass
    def play(self):
        print("PLAYING_ADD")
        self.ids['back'].text = "DONE"
        time.sleep(1)
        MDApp.get_running_app().root.current ="Page"

class Page(Screen):
    def __init__(self, **kw):
        super(Page, self).__init__(**kw)
        self.FM = File_man()
        self.sp_cards = ["0","1","2","3"]
        self.ads_bank = ""
        self.ads_count = 0
#        self.ids['spc'].text = "SP_CARDS: "+str(self.ads_count)

    def move(self):
        print("[GAME_STARTED]")
        MDApp.get_running_app().root.current ="MainWidget"
        self.FM.write_file("GAME.txt", "START@", "w")
    #OFFER_WALL
    #************^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def ads(self):
        if self.ads_count == 3:
            print("OUT_OF_ADS")
            return
#            self.ids[AdsBank].disabled=True
        print("PLAYING ADD")
        self.ads_count+=1
        MDApp.get_running_app().root.current ="AdsBank"


        if self.ads_count == 1:
            self.ads_bank += "ONE"
            self.FM.write_file("ADS_BANK.txt", self.ads_bank, "w")
        if self.ads_count == 2:
            self.ads_bank += "TWO"
            self.FM.write_file("ADS_BANK.txt", self.ads_bank, "w")
        if self.ads_count == 3:
            self.ads_bank += "THREE"
            self.FM.write_file("ADS_BANK.txt", self.ads_bank, "w")

        print("ADD COMPLETE:: \nCOUNT:: ",self.ads_count)

class MyMDApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #IMPORT CONTROL
        self.FM = File_man()
        self.conn = connections()
        self.FM.write_file("GAME.txt", "", "w")
        self.FM.write_file("SERVER.txt", "", "w")
        self.FM.write_file("ADS_BANK.txt", "", "w")


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

        self.AB = AdsBank()
        screen = Screen(name="AdsBank")
        screen.add_widget(self.AB)
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