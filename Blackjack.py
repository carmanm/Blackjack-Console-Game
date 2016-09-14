from tkinter import ttk
from tkinter import *
import random
import time


class blackjack:
    def __init__(self):                    
        global money
        
        money = 100
        
        begin = input("Welcome to the console version of blackjack, press enter to begin. . .")
        if begin == "":                        
            self.placeBet()
        else:
            really = input("That is not pressing enter. . . PRESS ENTER TO BEGIN. . .")
            if really == "":
                self.placeBet()
            else:
                print("Goodbye. . .")
                time.sleep(3)
                

    def placeBet(self):
        global money
        global bet
        
        print("you have $" + str(money))

        if money <= 0:
            print("Sorry, you're out of money. . .")
            print("Goodbye. . .")
            time.sleep(3)
            exit()
        
        time.sleep(0.5)
        print("_____________________________________________________________________")
        bet = input("Enter your bet: ")

        if bet == "" or bet.isalpha():
            print("Enter a number . . .")
            self.placeBet()

        if int(bet) > money:
            print("You don't have enough money. . . ")
            self.placeBet()
        
        money = money - int(bet)
        time.sleep(0.5)
        print("Remaining balance: ", money)
        time.sleep(0.5)
        getCards = input("Press enter to deal cards. . . ")
        if getCards == "":
            self.dealCards()
        else:
            ye = input("Press enter. . .")
            if ye == "":
                self.dealCards()
            else:
                print("You messed it all up. . .")
    
    def dealCards(self):
        global deck
        global total
        global deal1
        global deal2
        global currentHand
        global aceHand
        
        
        deck = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":"J", "K":"K", "Q":"Q", "A":"A"}

        
        
        print("Cards Dealt:")

        time.sleep(0.5)
        
        deal1 = random.choice(list(deck.keys()))
        deal2 = random.choice(list(deck.keys()))
        pair = print(deal1, ",", deal2)

        currentHand = [deal1, deal2]
        
        if deal1 == "J":
            deal1 = 10
        if deal1 == "K":
            deal1 = 10
        if deal1 == "Q":
            deal1 = 10
        if deal1 == "A":
            deal1 = 11

        if deal2 == "J":
            deal2 = 10
        if deal2 == "K":
            deal2 = 10
        if deal2 == "Q":
            deal2 = 10
        if deal2 == "A":
            deal2 = 11
            
        #acehand
        if deal1 == 11:
            ace1 = 1
        else:
            ace1 = deal1

        if deal2 == 11:
            ace2 = 1
        else:
            ace2 = deal2

        aceHand = [ace1, ace2]

        
        
        #print(aceHand)
        total = deal1 + deal2

        
                
        #print(total)
        if total == 21:
            time.sleep(1)
            print("BLACKJACK")
            self.playerWin()
        else:
            self.hitStay()


            
    def hitStay(self):
        time.sleep(0.5)
        HS = input("Would you like to hit or stay? 'h' for hit, 's' for stay. . .")
        
        if HS == "h" or HS == "H":
            self.hit()

        if HS == "s" or HS == "S":
            self.dealer1()

        if HS !="h" or HS != "H" or HS != "s" or HS != "S":
            print("You must type 'h' or 's'")
            time.sleep(0.5)
            self.hitStay()
                
    
    def hit(self):
        global deck
        global total
        global deal1
        global deal2
        global currentHand
        global aceHand
        
        deal3 = random.choice(list(deck.keys()))

        currentHand.insert(0, deal3)
        for value in currentHand:
            print(value, end = " , ")
            
        print("\n")
        
        if deal3 == "J":
            deal3 = 10
        if deal3 == "K":
            deal3 = 10
        if deal3 == "Q":
            deal3 = 10
        if deal3 == "A":
            deal3 = 11
        
        if total > 21 and deal3 == "A":
            deal3 = 1       
        
        
        total = total + deal3
        #print(total)

        if deal3 == 11:
            ace3 = 1
        else:
            ace3 = deal3    

        for i in aceHand:
            if i == "A":
                i = 1
               
        aceHand.insert(0, ace3)

        if "A" in currentHand:
            total = sum(aceHand)
            
        #print(aceHand)
        #print("CURRENT: ", currentHand)
        #print("SUM: ", total)
        
        
        if total > 21:
            time.sleep(1)
            print("BUST")
            print("Dealer wins. . .")
            self.placeBet()
        if total == 21:
            time.sleep(1)
            print("BLACKJACK")
            self.playerWin()
        if total < 21:
            self.hitStay()

    

    def playerWin(self):
        global money
        global bet
        
        money = money + (int(bet) * 2)

        self.placeBet()       

    def dealer1(self):
        global deck
        global total
        global _total
        global _deal1
        global _deal2

        time.sleep(1)          
    
        print("Dealer's turn:")

        time.sleep(0.5)
        
        _deal1 = random.choice(list(deck.keys()))
        _deal2 = random.choice(list(deck.keys()))
        _pair = print(_deal1, _deal2)

        time.sleep(0.5)

        if _deal1 == "J":
            _deal1 = 10
        if _deal1 == "K":
            _deal1 = 10
        if _deal1 == "Q":
            _deal1 = 10
        if _deal1 == "A":
            _deal1 = 11

        if _deal2 == "J":
            _deal2 = 10
        if _deal2 == "K":
            _deal2 = 10
        if _deal2 == "Q":
            _deal2 = 10
        if _deal2 == "A":
            _deal2 = 11

        _total = _deal1 + _deal2

                
        if _total == 21:
            time.sleep(1)
            print("BLACKJACK")
            print("Dealer wins. . .")
            self.placeBet()
            
        else:
            self.dealerPonders()


    
    
        


    def dealerPonders(self):
        global deck
        global total
        global _total
        global deal1
        global deal2
        global bet
        global money

        if total > _total:
            self.dealerHit()
        elif total == _total:
            time.sleep(1)
            print("Push. . .")

            money = money + int(bet)
            
            self.placeBet()

        if _total > total:
            print("Dealer wins. . .")
            self.placeBet()
        

    def dealerHit(self):
        global deck
        global total
        global _total
        global _deal1
        global _deal2
        
        _deal3 = random.choice(list(deck.keys()))

        print("HIT:", _deal3)

        if _deal3 == "J":
            _deal3 = 10
        if _deal3 == "K":
            _deal3 = 10
        if _deal3 == "Q":
            _deal3 = 10
        if _deal3 == "A":
            _deal3 = 11
        
        _total = _total + _deal3

        time.sleep(1)
        
        

        time.sleep(1)
        if _total > 21 and _deal3 == "A":
            _deal3 = 1  
        if _total > 21 and _deal1 == "A":
            _deal1 = 1
            #print(_total)
            self.dealerPonders()
        if _total > 21 and _deal2 == "A":
            _deal2 = 1
            #print(_total)
            self.dealerPonders()
        if _total > 21:
            time.sleep(1)
            print("BUST")
            self.playerWin()
        if _total == 21:
            time.sleep(1)
            print("BLACKJACK")
            print("Dealer wins. . .")
            self.placeBet()
        if _total < 21:
            self.dealerPonders()
        
        time.sleep(0.5)

        
        
        
            
def main():
    blackjack()

    exit()

if __name__ == "__main__": main()
