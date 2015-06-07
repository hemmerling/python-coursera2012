#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   coursera2012
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @version   1.00
#  @date      2015-01-01
#  @copyright Apache License, Version 2.0
#
#  Implementation of the game
#  "Blackjack"
#  for the Coursera course
#  "An Introduction to Interactive Programming in Python"
#
#  As I used PyUnit for external testing, some functions 
#  may contain extra code to accompish that,
#  e.g. "apparently unnecessary extra" return values,
#  "apparently unnecessary extra" split of functions,
#  "apparently unnecessary" complicated implementation of code,
#  some few print commands for traditional "print on console"
#  testing are in comments.
#
#  Copyright 2012-2015 Rolf Hemmerling
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""

# 1 Import modules
import simplegui
import random

# 2 Initialize global variables

# Initialisation of the random generator
# on my computer, by this, the result of
# random.randrange(self.randomStartValue,self.randomStopValue,1)
# - is always "1" on Python 2.7.3, at first run.
# - is always "2" on ColdeSkulptor, at first run.
# The cards are
# ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK', 'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK']
# After shuffle
# ['S8', 'HT', 'H2', 'CQ', 'H9', 'HQ', 'S5', 'C4', 'SJ', 'CK', 'H4', 'DK', 'D5', 'SQ', 'H8', 'HK', 'D3', 'C7', 'S4', 'D2', 'DJ', 'ST', 'HA', 'H6', 'D7', 'C8', 'H5', 'S3', 'C5', 'H7', 'DQ', 'D6', 'SA', 'C9', 'S7', 'CA', 'S9', 'DA', 'CJ', 'DT', 'D8', 'C2', 'S6', 'C3', 'CT', 'C6', 'D9', 'D4', 'SK', 'S2', 'HJ', 'H3']
# With pop(), the most right value is taken from the list.

myRandomSeed = 3 

# Initialize some useful global variables
in_play = False
outcome = ""
score = 0

# Define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)

# Global class instances
my_deck = None
my_hand = None
my_bank = None

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0]+CARD_CENTER[0],pos[1]+CARD_CENTER[1]], CARD_SIZE)
        return

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], 
                    CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# define hand class
class GenericHand:
    """ Hand of cards """

    # List of cards, kept by the hand
    cards = []
    
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = []
        for counter in range(len(self.cards)):
            ans.append(self.cards[counter].__str__())
        return str(ans)

    def add_card(self, card):
        self.cards.append(card)
        return
    
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        generic_hand_value = 0
        has_ace = False
        for card in self.cards:
            card_value = VALUES[card.get_rank()]
            if (not has_ace):
                has_ace = (card_value == 1)
            generic_hand_value += card_value
        if (has_ace and ((generic_hand_value+10) <= 21)):
            generic_hand_value += 10
        return generic_hand_value

    def busted(self):
        return	# replace with your code
    
# define bank class
class Bank(GenericHand):
    """ Bank """
    def draw(self, canvas, p):
        global in_play
        first_card = in_play
        # If first card is still covered, display card back
        for card in self.cards:
            if (first_card):
                card.draw_back(canvas, p)
                first_card=False
            else:
                card.draw(canvas, p)
            p[0] +=100
        return
    
# define hand class
class Hand(GenericHand):
    """ Hand """
    def draw(self, canvas, p):
        for card in self.cards:
            card.draw(canvas, p)
            p[0] +=100
        return

# define deck class
class Deck:
    """ Deck of cards """

    # List of cards, kept in the deck
    cards = []
    
    # Create a fresh deck of (sorted) cards
    def create_deck(self):
        created_cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        return created_cards
    
    def __init__(self):
        self.cards = self.create_deck()

    def __str__(self):
        ans = []
        for counter in range(len(self.cards)):
            ans.append(self.cards[counter].__str__())
        return str(ans)
        
    # add cards back to deck and shuffle
    def shuffle(self):
        global myRandomSeed
        #random.seed(myRandomSeed)
        #self.__init__()
        random.shuffle(self.cards)
        return
    
    # take a card from deck
    def deal_card(self):
        card = self.cards.pop()
        return card 

class BlackJackGame():
    """ Implementation of the game BlackJack """
    
    # 3 initialize class globals
    
    # 4 Helper functions to initialize game   
    def init(self):
        global card_images, card_back, score       
        card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
        card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

        self.deal()
        # Score is just reset at start of game
        score = 0
        
        return 

    #define event handlers for buttons
    def deal(self):
        global outcome, in_play, number_of_cards_in_deck
        global my_deck, my_hand, my_bank
        global score
                    
        # your code goes here
        # Create deck, hand, bank
        my_deck = Deck()
        my_hand = Hand()
        my_bank = Bank()

        # Start new game, so first card of dealer is covered
        hidden_card=True

        # If you press the Deal button within the game, you loose your hand
        if (in_play):
            score -=1
            outcome = "Deal Button pressed - You lost."
            # Display of this message just on the console
            print outcome
            outcome = ""
        else:
            # No display of a result message
            outcome = ""

            # Load new card deck and shuffle cards
        my_deck.shuffle()
        
        in_play = True

        print "New deal!"
        self.hit_bank()
        self.hit_bank()
        
        self.hit()
        self.hit()    

        number_of_cards_in_deck = len(my_deck.cards)

        return

    
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    def hit(self):
        global in_play, score, outcome, my_hand
        if (in_play):
            card = my_deck.deal_card()
            my_hand.add_card(card)        
            # update number of cards in deck
            number_of_cards_in_deck = len(my_deck.cards)
            print "Hand: ", my_hand.__str__(), " ", my_hand.get_value()
            if (my_hand.get_value()>21):
                score -=1
                in_play = False
                outcome = "You went bust and lose."
                print outcome, "\nScore ", score, "\nNew deal?\n"
        else:
            card = None
            print outcome, "\nScore ", score, "\nNew deal?\n"
        return card

    # Pass a card from deck to bank
    def hit_bank(self):
        global in_play 
        card = my_deck.deal_card()
        my_bank.add_card(card)
        # you can remove the comment of next line, for cheating :-)
        #print "Dealer: ", my_bank.__str__(), " ", my_bank.get_value()
        return card
       
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    def stand(self):
        global in_play, score, outcome
        if (in_play):
            while (my_bank.get_value() < 21-4):
                self.hit_bank()
            in_play = False
            if (my_hand.get_value()>21):
                outcome = "You went bust and lose."
            elif (my_bank.get_value()>21): 
                outcome = "The dealer went bust. You win."
                score +=1
            elif (my_hand.get_value()>my_bank.get_value()):
                outcome = "You win."
                score +=1
            else:
                outcome = "You lose."
                score -=1
            print "Dealer: ", my_bank.__str__(), " ", my_bank.get_value()
        print outcome, "\nScore ", score, "\nNew deal?\n"
        return

    # 5 Define event handlers

    def draw(self, canvas):
        """ Draw Handler """
        global number_of_cards_in_deck
        canvas.draw_text("Blackjack", (100, 100), 36, "Aqua")
        canvas.draw_text("Score", (400, 100), 24, "Black")
        canvas.draw_text(str(score), (500, 100), 24, "Black")
        canvas.draw_text("Dealer", (25, 175), 24, "Black")
        canvas.draw_text("Player", (25, 375), 24, "Black")
        
        if (in_play):
            canvas.draw_text("Hit or stand?", (150, 375), 24, "Black")
        else:
            canvas.draw_text("New deal?", (150, 375), 24, "Black")
        canvas.draw_text(outcome, (150, 175), 24, "Black")

        canvas.draw_text("# of cards in deck: "+str(len(my_deck.cards)), (25, 550), 24, "Black")
        
        # test to make sure that card.draw works, replace with your code below       
        #card = Card("H", "3")
        #card.draw_back(canvas, [75, 200])
        #card = Card("H", "J")
        #card.draw(canvas, [175, 200])
        #card = Card("S", "2")
        #card.draw(canvas, [75, 400])
        #card = Card("S", "K")
        #card.draw(canvas, [175, 400])
        #card = Card("D", "4")
        #card.draw(canvas, [275, 400])

        my_hand.draw(canvas, [25, 400])
        my_bank.draw(canvas, [25, 200])

        return
     
    # This function is executed to start the application
    def main(self):
        """ Class start function """
        # 6 Create frame
        global frame
        frame = simplegui.create_frame("Blackjack", 600, 600)
        frame.set_canvas_background("Green")
        # 7 Register event handlers for control elements
        frame.set_draw_handler(self.draw)
        frame.add_button("Deal", self.deal, 200)
        frame.add_button("Hit",  self.hit, 200)
        frame.add_button("Stand", self.stand, 200)

        # deal an initial hand

        # 8 Start frame
        self.init()
        frame.start()
        return 

# always remember to check your completed program against the grading rubric
