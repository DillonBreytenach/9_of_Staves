#TODO:::  
######## 1) LOAD DECK
######## 2) ALLOCATE SELECTED CARD TO CORRECT TAB_PLACEMENT
######## 3) F_Tree CREATOR

#LIB REQD IMPORTS
from functools import partial
import time
import string
import threading
#KIVY IMPORTS
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.scrollview import ScrollView
#MY IMPORTS
from file_handle_C import File_man
from conns import connections

Window.size = (300, 560)

#*********************************************************
class Game(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Rec = Recycle()
        self.FM = File_man()
        self.details()
        #
        self.TURN = False
        Clock.schedule_interval(partial(self.ft_UPDATER), 1)



    def pos_update(self, move):
        print("\n***********************************************\nUPDATING\n")
        try:
            self.FM.write_file("GAME.txt", move, "w")
            self.ids.OPP.text='ACTIVE'+'\nOPP_TURN'
            self.turn = False
            print("\n\n     *****UPDATED*****\n\n*************************************\n", move)
            return "DONE"
        except:
            print("POSITION_CHANGE [NOT_UPDATED]")
            pass


    def ft_UPDATER(self, inst):
        print("GETTING UPDATES", str(inst))
        server_data = self.FM.read_file("SERVER.txt")

        try:
            print("UPDATING OPP DATA")
            OppData = str(self.FM.read_file("OppData.txt"))
            Opp_Data = OppData.split("@")
            self.ids['oppName'].text = str(Opp_Data[1])
            self.ids['oppIcon'].text = str(Opp_Data[2])
        except Exception as e:
            print("OPP_DATA:ERROR:ft_UPDATER:: ", str(e))


        
        print("SERVER_DATA:: /")
        for i, _ in enumerate(server_data):
            print(f"DATA:{str(i)}: {str(_)}")
            
        # ASSIGN CARDS TO WIDGETS -> DECK (230, 250)
        # ON CLICK -> MOVE CARD TO RESPECTIVE TAB SLOT



    def details(self):
        my_data = str(self.FM.read_file("Player.txt"))
        print("MY_DETAILS:: ", str(my_data))
        mdata = my_data.split("@")
        try:
            #ICON IMAGE HERE
            self.ids['myIcon'].text = str(mdata[3])
                            #^^^^^^^^^^    ^^^
            self.ids['myName'].text = str(mdata[0]).translate(str.maketrans('','',string.punctuation))
        except Exception as e:
            print("myIcon:Loading:Error: ", str(e))

    def home_it(self):
        self.FM.write_file("GAME.txt", "QUIT", "w")
        self.pos_update("QUIT")
        time.sleep(1.5)
        self.FM.write_file("SERVER.txt", "", "w")
        self.FM.write_file("game_over.txt", "", "w")
        self.FM.write_file("GAME.txt", "", "w")
        MDApp.get_running_app().root.current = 'Home'

    def at_hand(self):
        print("CARD TOUCHED")

class TABS(TabbedPanel):
    pass

class Recycle(ScrollView):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass
    def card(self):
        print("TOUCHED")
class RecycleOne(ScrollView):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass
    def card(self):
        print("TOUCHED")
class RecycleTwo(ScrollView):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass
    def card(self):
        print("TOUCHED")

class Score(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FM = File_man()
        win = str(self.FM.read_file("game_over.txt"))
        #print("WIN:?0", win)
        self.ids['back'].text = str(win)
        #print("DONE")


    def home(self):
        self.FM.write_file("GAME.txt", "END", "w")
        time.sleep(5)
        self.FM.write_file("SERVER.txt", "", "w")
        self.FM.write_file("GAME.txt", "", "w")
        self.FM.write_file("game_over.txt", "", "w")
        MDApp.get_running_app().root.current = "Home"
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class AdsBank(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass
    def play(self):
        print("PLAYING_ADD")
        self.ids['back'].text = "DONE"
        time.sleep(1)
        MDApp.get_running_app().root.current ="Page"

class Home(Screen):
    def __init__(self, **kw):
        super(Home, self).__init__(**kw)
        self.FM = File_man()
        self.sp_cards = ["0","1","2","3"]
        self.ads_bank = ""
        self.ads_count = 0
        self.on_start()

    def test_recyle(self):
        MDApp.get_running_app().root.current = 'Game'

    def on_start(self):
        self.NAME = str(self.FM.read_file("Player.txt"))
        name = self.NAME.split("@")
        try:
            user = str(name[0]).translate(str.maketrans('','',string.punctuation))
            icon = str(name[3]).translate(str.maketrans('','',string.punctuation))
            print("NAME:: ", str(user))
            self.ids['Player'].text = str(user)
            self.ids['Icon_'].text = str(icon)
        except Exception as e:
            print("PROFILE_ERROR:HOME_SCREEN: ", str(e))

    def move(self):
        MDApp.get_running_app().root.current = 'Lobby'

    def LR(self):
        MDApp.get_running_app().root.current ="LR"


    #OFFER_WALL
    #************^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def ads(self):
        if self.ads_count == 3:
            print("OUT_OF_ADS")
            return
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

class Lobby(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FM = File_man()

    def Back(self):
        print("BACK_TO_LOADING")
        MDApp.get_running_app().root.current = 'Home'

    def Lobb(self):
        ready = []
        c = 0
        while True:
            time.sleep(0.001)
            ready = self.FM.read_file("SERVER.txt")
#            print(ready)
            if "MATCH" in str(ready):
                return "GO"
            if c >= 10000:
                return
            else:
                c += 1
#                print("WAITING FOR MATCH..", str(c))
                self.ids['Lobby'].text = "WAITING FOR MATCH"

    def Ready(self):
        print("READY..")
        me = str(self.FM.read_file("Player.txt"))
        mi = me.split("@")
        try:
            print("SENDING PROFILE:: ")
            for _ in mi:
                print("P:: ", str(_))
            name = str(mi[0]).translate(str.maketrans('','',string.punctuation))
            icon = str(mi[3]).translate(str.maketrans('','',string.punctuation))
            data = "START@"+name+"@"+icon
            self.FM.write_file("GAME.txt", data, "w")
        except Exception as e:
            print(str(e))
        time.sleep(5)
        ready = str(self.FM.read_file("SERVER.txt"))
        print(ready)
        if "MATCH" in ready:
            MDApp.get_running_app().root.current = "Game"
        else:
            if "GO" in str(self.Lobb()):
                MDApp.get_running_app().root.current = "Game"

class Register(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FM = File_man()
        self.conns = connections()
        self.gender = ""
        self.selected = False

    def icon_select(self, inst):
        if self.selected == True:
            self.selected = False
            self.ids['Male'].disabled = False
            self.ids['Female'].disabled = False


            return
        if "Male" in inst and self.selected == False:
            self.gender = "Male" 
            print(":SET:ID:icon:", str(self.gender))
            self.ids['Female'].disabled = True
            self.selected = True
            return
        if "Female" in inst and self.selected == False:
            self.gender = "Female" 
            print(":SET:ID:icon:", str(self.gender))
            self.ids['Male'].disabled = True
            self.selected = True
            return

    def select_Icon(self, day, month):
        try:
            
            day = int(day)
            month = int(month)
            if day>=21 and month >=3 and month <= 4:
                print("WHAT DA POES")
            print(f"\n\n\nVALS --{day}:{month}--", "\n\n*************************************")


            if month >= 3 and month <=4:#MARCH
                if day <= 19 or day >= 21:#APRIL
                    return "Aries"
            elif month >=4 and month <=5:#APRIL 
                if  day >= 20 or day <=20:#MAY 
                    return "Taurus"
            elif month >= 5 and month <= 6:#MAY 
                if  day >= 21 or day <= 20:#JUNE 
                    return "Gemini"
            elif month >=6 and month <=7 :#JUNE 
                if day >=21 or day <=22:#July 
                    return "Cancer"
            elif month >= 7 and month <= 8:#JULY 
                if day >= 23 or day <= 22:#AUGUST 
                    return "Leo"
            elif month >=8 and month <=9:#AUGUST 
                if day >= 23 or day <=22:#SEPTEMBER 
                    return "Virgo"
            elif month >=9 and month <= 10:#SEPTEMBER 
                if day >= 23 or day <= 22:#OCTOBER 
                    return "Libra"
            elif month >= 10 and month <= 11:#OCTOBER 
                if day >=23 and day <= 21:#NOVEMBER 
                    return "Scorpio"
            elif month >= 11 and month <= 12:#NOVEMBER 
                if day >= 22 or day <= 21:#DECEMBER 
                    return "Sagittarius"
            elif month >= 12 and month <= 1:#DECEMBER 
                if day >= 20 or day <= 18:#JANUARY 
                    return "Capricorn"
            elif month >= 1 and month <= 2:#JANUARY 
                if day >= 19 or day <= 18:#FEBUARY 
                    return "Auqarius"
            elif month >= 2 and month <= 3:#FEBUARY 
                if day >= 19 or day <= 20:#MARCH 
                    return "Pisces"
        except Exception as e:
            print("ICON:SELECTION::ERROR:: ", str(e))

    def Register(self):
        print("REGISTER_ED: NOT_YET_UPDATED")
        name = str(self.ids['Name'].text)+"@"
        day = str(self.ids['Day_Date'].text)
        month = str(self.ids['Month_Date'].text)
        year = str(self.ids['Year_Date'].text)+"@"


        Icon = str(self.select_Icon(day, month))
        print("ICON MADE:: ", str(Icon))

        Count = str(self.ids['Country'].text)+"@"
        player_data = name+day+"#"+month+"#"+year+Count+Icon
        self.FM.write_file("Player.txt", player_data, "w")
        if "DONE" in str(self.conns.send_msg("Player.txt")):
            print("WAITING FOR SERVER")
            try:
                rec = self.conns.get_msg("GET")
                print("RECV:: ", str(rec))
                if "WELCOME" in rec:
                    print("WELCOME")
                    H= Home()
                    H.on_start()
                    MDApp.get_running_app().root.current ="Welcome"
            except Exception as e:
                print("LOADING PROFILE:ERROR: ",str(e))
                pass

class Welcome(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FM = File_man()

        self.pl = self.FM.read_file("Player.txt")
        print(str(self.pl))
        
    def home(self):
        MDApp.get_running_app().root.current ="Home"

class Login(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FM = File_man()
        self.conns = connections()

    def go(self):


        name = str(self.ids['Name'].text)+"@"
        birth = str(self.ids['Date'].text)+"@"
        player_data = name+birth
        
        
        self.FM.write_file("Player.txt", player_data, "w")

        
        if "DONE" in str(self.conns.send_msg("Player.txt")):
            print("WAITING FOR SERVER")
            try:
                rec = self.conns.get_msg("GET")
                print("RECV:: ", str(rec))



                if "NEW" in rec:
                    print("WELCOME_NEW")
                    MDApp.get_running_app().root.current ="Register"
                if "OLD" in rec:
                    print("WELCOME_BACK")
                    H = Home()
                    H.on_start()
                    MDApp.get_running_app().root.current ="Home"

            except Exception as e:
                print("LOADING PROFILE:ERROR: ",str(e))
                pass

class LR(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    
    
    def Login(self):
        MDApp.get_running_app().root.current ="Login"

    def Register(self):
        MDApp.get_running_app().root.current ="Register"

class Loading(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FM = File_man()

    def Start(self):
        pl = self.FM.read_file("Player.txt")
        if len(str(pl)):            
            MDApp.get_running_app().root.current ="Home"
        else:
            MDApp.get_running_app().root.current ="LR"


#MAIN
class MyMDApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #IMPORT CONTROL
        self.FM = File_man()
        self.conn = connections()
        self.FM.write_file("GAME.txt", "", "w")
        self.FM.write_file("SERVER.txt", "", "w")
        self.FM.write_file("ADS_BANK.txt", "", "w")

        #TO BE MOVED TO LOADING....
        self.recv = threading.Thread(target=self.conn.get_msg, args=('RUN',))
        self.watch = threading.Thread(target=self.conn.send_msg, args=('RUN',))
        try:
            print("STARTING_CONNECTION(s)")
            self.recv.start()
            self.watch.start()
        except:
            print("\n\n!!INIT_CONNECTION_ERROR!!\n\n")
        # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

    def build(self):
        #REMEMBER TO UPDATE ALL FILES ON STARTUP
        Builder.load_file("main.kv")

        self.screenM = ScreenManager()

        self.SC = Score()#END OF GAME SCREEN
        screen = Screen(name="Score")
        screen.add_widget(self.SC)
        self.screenM.add_widget(screen)


        self.Re = Recycle() #MATCH_SCREEN...
        screen = Screen(name="Recycle")
        screen.add_widget(self.Re)
        self.screenM.add_widget(screen)

        self.G = Game() #MATCH_SCREEN...
        screen = Screen(name="Game")
        screen.add_widget(self.G)
        self.screenM.add_widget(screen)

        self.Lob = Lobby()
        screen = Screen(name="Lobby")
        screen.add_widget(self.Lob)
        self.screenM.add_widget(screen)

        self.AB = AdsBank()
        screen = Screen(name="AdsBank")
        screen.add_widget(self.AB)
        self.screenM.add_widget(screen)

        self.W = Welcome()
        screen = Screen(name="Welcome")
        screen.add_widget(self.W)
        self.screenM.add_widget(screen)

        self.R = Register()
        screen = Screen(name="Register")
        screen.add_widget(self.R)
        self.screenM.add_widget(screen)

        self.P = Login()
        screen = Screen(name="Login")
        screen.add_widget(self.P)
        self.screenM.add_widget(screen)

        self.H = Home()
        screen = Screen(name="Home")
        screen.add_widget(self.H)
        self.screenM.add_widget(screen)

        self.LR = LR()
        screen = Screen(name="LR")
        screen.add_widget(self.LR)
        self.screenM.add_widget(screen)

        
        self.L = Loading()
        screen = Screen(name="Loading")
        screen.add_widget(self.L)
        self.screenM.add_widget(screen)


        self.screenM.current="Loading"

        return self.screenM

if __name__=="__main__":
    M = MyMDApp()
    M.run()