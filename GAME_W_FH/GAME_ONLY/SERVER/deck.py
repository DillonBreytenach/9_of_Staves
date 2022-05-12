import random


class Deck():
    def __init__(self, *args):
        super(Deck, self).__init__(*args)
        #31 crads total
        #12 t_M_B
        #3 jokers
        #3 x 6 runes cards

        #LIST OF CARDS
        self.card1 = ["CARD1", False, ""]
        self.card2 = ["CARD2", False, ""]
        self.card3 = ["CARD3", False, ""]
        self.card4 = ["CARD4", False, ""]
        self.card5 = ["CARD5", False, ""]
        self.card6 = ["CARD6", False, ""]
        self.card7 = ["CARD7", False, ""]
        self.card8 = ["CARD8", False, ""]
        self.card9 = ["CARD9", False, ""]
        self.card10 = ["CARD10", False, ""]
        self.card11 = ["CARD11", False, ""]
        self.card12 = ["CARD12", False, ""]
        self.card13 = ["CARD13", False, ""]
        self.card14 = ["CARD14", False, ""]
        self.Deck_List = [self.card1,
                          self.card2,
                          self.card3,
                          self.card4,
                          self.card5,
                          self.card6,
                          self.card7,
                          self.card8,
                          self.card9,
                          self.card10,
                          self.card11,
                          self.card12,
                          self.card13,
                          self.card14]


    def shuffleDeck(self):
        for cardpos in range(len(self.Deck_List)):
            randPos = random.randint(0, 13)
            self.Deck_List[cardpos], self.Deck_List[randPos] = self.Deck_List[randPos], self.Deck_List[cardpos]
            DECK = self.Deck_List
            return DECK

    def get_card(self, user, DECK):
        r_card = []
        card_val = ""
        card_set = bool
        pl = str(user)
        i = 0
        while i <= 13:
            
            if DECK[i][1] == False and  len(str(DECK[i][2])) <2 :
                print("BEFORE:  ",DECK[i])
                card_val = DECK[i][0]
                DECK[i][1] = True
                card_set = DECK[i][1]
                DECK[i][2] = user
                pl = DECK[i][2]
                r_card = [card_val, card_set, pl]
                return r_card, DECK
            i+=1
