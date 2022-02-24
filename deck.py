import random
from random import randint

class Deck():
    def __init__(self, name, deck):
        super().__init__(name, deck)
        

    def build_deck(name):
        print("Building Deck for {}".format(name))

        # Build Deck FTPhase
        deck = []
        sleves = ["FTree"]
        Values = [1, 2, 3]
        creations = ["Joker"]
        FTRune = ["All-giz", "Har-gool", "Yah-rah"]

        for i in range(12):
            for sleve in sleves:
                for value in Values:
                    card_val = "{} {}".format(sleve, value)
                    deck.append(card_val)

        for i in range(3):
            for sleve in sleves:
                for creation in creations:
                    card_val ="{} {}".format(sleve, creation)
                    deck.append(card_val)

        for i in range(3):
            deck.append(FTRune[0])
            deck.append(FTRune[1])
            deck.append(FTRune[2])
        return deck

        

    #Shuffle the Deck
    def shuffle_deck(deck):
        for cardpos in range(len(deck)):
            randpos = random.randint(0, 47)
            deck[cardpos], deck[randpos] = deck[randpos], deck[cardpos]
        print("Deck shuffled")

        return deck