from random import *
from deck import Deck


# main file/function to initiate game 
class main():
    def __init__(self, name, deck):
        #Objects
        self.name = name
        pass

    #Greet players and create player object
    def greet():
        greet = "Hello Newbi; What's your name: "
        name = input(greet)
        print("Hello {}".format(name))
        deck = Deck.build_deck(name)
        print("deck:")
        print(deck)
        print("_____________\n\n")
        
        deck = Deck.shuffle_deck(deck)
        print("Deck:")
        print(deck)

    def print_deck():
        pass



if __name__=='__main__':
    main.greet()
