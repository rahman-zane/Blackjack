# -*- coding: utf-8 -*-
###BLACKJACK GAME 

#Created on Mon Aug 19 13:31:24 2019

#@author: Rahman Al-Shabazz

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks= ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#Class Definitions
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                  
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The deck has:' + deck_comp
                            
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card  
                            
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        
    def hit(self,card):
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1
    
    def __str__(self):
        hand_comp = ''
        for card in self.hand:
            hand_comp += card.__str__()+'\n'
        return hand_comp
    
class Bank:
    def __init__(self):
        self.budget = 500
        
    def bet(self,amount):
        self.budget -= amount
        self.amount = amount

    def win_bet(self, bet_amount):
        self.bet_winnings = 2*bet_amount
        print('Congratulations! You have won this bet!\nAccount Balance is {}'.format(self.budget+self.bet_winnings))

    def lose_bet(self):
        print('Sorry, maybe next time!\nAccount Balance is {}'.format(self.budget))

#function definitions
bank = Bank()
okay_amount = False
def take_bet():
    #input a bet that is within the users budget
    okay_amount = False
    while okay_amount == False:
        try:
            amount = int(input('How much would you like to bet (Budget = {})?: £'.format(bank.budget)))
        except:
            print('Please enter a numerical value.')
        else:
            if amount > bank.budget:
                print('Please enter a numerical value within your budget, £{}'.format(bank.budget))
                okay_amount = False
            else:
                okay_amount = True
                return amount
            
#dealing the initial hand
def initial_deal():
    full_deck.shuffle()
    for i in range(2):
        dealers_hand.hit(full_deck.deal())
        players_hand.hit(full_deck.deal())
    print("Dealer's Card:\n<hidden>\n{}\n".format(dealers_hand.hand[1]))
    print("Your Cards:\n{}\n{}\n".format(players_hand.hand[0],players_hand.hand[1]))

            
def hit_or_miss():
    #get correct entry for hit or miss option and perform hit or miss
    inpt = False
    full_deck.shuffle()
    while inpt == False:
        try:
            a = str(input('Would you like to hit or miss? \n'))
        except:
            print('Please type hit or miss')
        else:
            if a.upper()[0] == 'H':
                players_hand.hit(full_deck.deal())
                for i in range(len(players_hand.hand)):
                    print(players_hand.hand[i])
                if players_hand.value > 21:
                    print("You've gone bust, you lose!")
                    game_on = False
                
            elif a.upper()[0] == 'M':
                for i in range(len(players_hand.hand)):
                    print(players_hand.hand[i])
                print("Your score: {}".format(players_hand.value))
                inpt = True
    
            else:
                print('Please type hit or miss')     
                
def deal_dealer(amount):
    while dealers_hand.value < 17:
        dealers_hand.hit(full_deck.deal())
        if dealers_hand.value < 22:
            pass
        else:
            print("Dealer's gone bust!")
            bank.win_bet(amount) 
            game_on = False
            
### GAME STARTS            
bank = Bank()
replay = True
while replay == True:
    game_on = True
    while game_on == True:
        print('Welcome to Blackjack! Get as close to 21 without going over')
        full_deck = Deck()
        dealers_hand = Hand()
        players_hand = Hand()
        amount = take_bet()
        bank.bet(amount)
        initial_deal()
        hit_or_miss()
        deal_dealer(amount)
        print("Dealer's score: {}\n".format(dealers_hand.value))
        if players_hand.value > dealers_hand.value:
            bank.win_bet(amount)
        else:
            bank.lose_bet
        game_on = False
    b = str(input('Would you like to play again, yes or no? '))
    if b.upper()[0] == 'N':
        replay = False

print('Thank you for playing!')