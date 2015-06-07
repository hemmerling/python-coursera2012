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
#  "Pairs"
#  for the Coursera course
#  "An Introduction to Interactive Programming in Python"
#
#  # Behaviour according to specs:
#  "In state 2, if you click on an unexposed card, 
#  that card is exposed and you switch to state 1".
#  "1 pt - The game ignores clicks on exposed cards".
#
#  By this I decided to implement:
#  In state 2, if you click on an exposed, even unpaired card, nothing happens.
#
#  As I used PyUnit for external testing, some functions 
#  may contain extra code to accompish that,
#  And I use a single class to enable testing with PyUnit.
#  Classes are not yet topic of week 5.
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
#
# card_pool = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
#
# is sorted to
# card_deck = [5, 3, 4, 8, 8, 7, 1, 2, 6, 6, 1, 7, 4, 3, 5, 2]  
#
# This results in cards order in the card_deck
# [7, 8, 3, 7, 2, 4, 1, 2, 1, 6, 1, 5, 8 4, 3, 6, 5]
myRandomSeed = 3

# Deck of cards
card_deck = []

# exposed_deck: entry is
#  True if the card is flipped over and its value is visible
#  False if the card's value is hidden.
exposed_deck = []

# State of the game
state = 0

# Index of drawn cards of current turn
currently_selected_cards = [None, None]

# Number of moves
moves = 0

# 3 Define classes
    
class PairsGame():

    # 3 initialize class globals
    WIDTH = 800
    HEIGHT = 200
    CARD_WIDTH = 50
    CARD_HEIGHT = 100
    CARD_LINEWIDTH = 3
    NUMBER_OF_PAIRS = 8
    CHARACTER_FONTSIZE = 12
    
    # The card pool, a deck of sorted cards
    card_pool = []
    
    # 4 Helper functions to initialize game   
    def init_card_pool(self):
        """ Initialize pool of cards with 2 pairs each """
        result = []
        for counter in range(0, self.NUMBER_OF_PAIRS):
            result +=[counter+1, counter+1]
        return result

    def init_card_deck(self, card_pool):
        """ Shuffle the card deck, sourced by the card pool """
        global myRandomSeed
        random.seed(myRandomSeed)
        result = card_pool
        random.shuffle(result)
        return result 

    def init_exposed(self,exposed_deck):
        """ Reset the list of exposed cards
            or set it with given exposed values """
        global last_turn
        global moves
        result = []
        if exposed_deck == None:
            for counter in range(0, self.NUMBER_OF_PAIRS*2, 1):
                result.append(False)
        else:
            result = exposed_deck
        # there was no last turn			
        currently_selected_cards = [None, None]
        # reset number of moves
        moves = 0
        return result
    
    def init(self):
        """ Initialization """
        global card_pool, card_deck, exposed_deck
        global state
        state = 0
        card_pool = self.init_card_pool()
        card_deck = self.init_card_deck(card_pool)
        #exposed_sample = [True, False, True, False, True, True, False, True, 
        #                  False, False, False, False, False, False, False, False]
        #exposed_deck = self.init_exposed(exposed_sample)
        exposed_deck = self.init_exposed(None)
        return  

    def coordinates_of_number(self, index):
        """ Returns the coordiantes for the number of a card """
        x_coordinate = index*self.CARD_WIDTH
        y_coordinate = self.CARD_HEIGHT+(self.HEIGHT-self.CARD_HEIGHT)/4
        return [x_coordinate, y_coordinate]

    def coordinates_of_nonexposed_card_corner(self, index, corner):
        """ Returns the coordinates of a corner of a nonexposed card """
        if (corner == 0):
            x_coordinate = index*self.CARD_WIDTH
            y_coordinate = 0+self.HEIGHT/4
        elif (corner == 1):
            x_coordinate = index*self.CARD_WIDTH+self.CARD_WIDTH
            y_coordinate = 0+self.HEIGHT/4
        elif (corner == 2):
            x_coordinate = index*self.CARD_WIDTH+self.CARD_WIDTH
            y_coordinate = self.CARD_HEIGHT+self.HEIGHT/4
        elif (corner == 3):
            x_coordinate = index*self.CARD_WIDTH
            y_coordinate = self.CARD_HEIGHT+self.HEIGHT/4
        else:
            x_coordinate = None
            y_coordinate = None
        return [x_coordinate, y_coordinate]

    def coordinates_of_nonexposed_card(self, index):
        """ Returns the coordinates of all corners of a nonexposed card """
        result = []
        result.append(self.coordinates_of_nonexposed_card_corner(index, 0))
        result.append(self.coordinates_of_nonexposed_card_corner(index, 1))
        result.append(self.coordinates_of_nonexposed_card_corner(index, 2))
        result.append(self.coordinates_of_nonexposed_card_corner(index, 3))
        return result
        
    def fontsize(self):
        """ Returns the font size of a card """
        return self.CARD_HEIGHT/2

    def show_state(self, canvas, current_state):
        """ Show current state on display """
        if current_state == 0:
            result = "Game beginning"
        elif current_state == 1:
            result = "One card exposed"
        else:
            result = "Two cards exposed"
        canvas.draw_text(result, [0, self.CARD_HEIGHT+self.HEIGHT/2-self.CHARACTER_FONTSIZE], self.CHARACTER_FONTSIZE, "White")
        return result
    
    def draw_card(self, canvas, coordinates, line_color, fill_color):
        """ Draw the card at the given coordinates """
        canvas.draw_polygon([coordinates[0], 
                             coordinates[1], 									 
                             coordinates[2],
                             coordinates[3]],
                             self.CARD_LINEWIDTH, line_color, fill_color)
        return coordinates, line_color, fill_color

    # cards are logically 50x100 pixels in size    
    def draw(self, canvas):
        """ Draw card """
        global card_deck, exposed_deck
        global state
        for counter in range(0, self.NUMBER_OF_PAIRS*2):
            exposed = exposed_deck[counter]
            coordinates = self.coordinates_of_nonexposed_card(counter)
            if (exposed):
                """ Draw card with red line color and white fill color,
                    card value as text, black letters """
                self.draw_card(canvas, coordinates, "Red", "White")
                card_coordinate = self.coordinates_of_number(counter)
                card_fontsize = self.fontsize()
                card_text = str(card_deck[counter])
                canvas.draw_text(card_text, card_coordinate, card_fontsize, "Black")
            else:
                """ Draw card with red line color and green fill color """
                self.draw_card(canvas, coordinates, "Red", "Green")
        self.show_state(canvas, state)
        return

    def state_handler(self, card_index):
        """ State handler """
        global state, card_deck, exposed_deck, currently_selected_cards, moves
        card_value = card_deck[card_index]
        exposed = exposed_deck[card_index]
        if state == 0:
            if (not exposed):
                exposed_deck[card_index] = True
                currently_selected_cards[0] = card_index
                state = 1
        elif state == 1:
            if (not exposed):
                exposed_deck[card_index] = True
                currently_selected_cards[1] = card_index
                state = 2
                # We just selected 2 cards, one turn is done
                # Remember with last pair of cards, 
                # this here is the last action ( no state = 2 )
                moves +=1   
        else:
            # Determine if the previous two cards are paired or unpaired. 
            exposed = exposed_deck[card_index]
            if (not exposed):
                if not (card_deck[currently_selected_cards[0]] ==
                        card_deck[currently_selected_cards[1]]    ):
                        exposed_deck[currently_selected_cards[0]] = False
                        exposed_deck[currently_selected_cards[1]] = False
                exposed_deck[card_index] = True
                currently_selected_cards[0] = card_index
                state = 1     
        return state, moves
    
    # 5 Define event handlers
    def mouseclick(self, pos):
        """ Mouseclick handler """
        global state, card_deck, currently_selected_cards
        global moves, label
        card_index = None
        card_value = None
        if (pos[1] > self.HEIGHT/4) and (pos[1] < self.HEIGHT/4 + self.CARD_HEIGHT):
            # Floor division to get the card index
            card_index = (pos[0] // self.CARD_WIDTH)
            card_value = card_deck[card_index] # just for PyUnit testing..
            if (card_index >= 0) and (card_index < len(card_deck)):
                # mouseclick on a card
                # please call the state handler to check for state change
                self.state_handler(card_index)                  
            else:
                # mouseclick too far right or left, not on a card
                pass
        else:
            # mouseclick below or above the cards
            pass
        label.set_text("Moves = "+str(moves))
        return card_index, card_value

    def init_gui(self):
        """ Intialize Graphics User Interface ( GUI )"""
        global frame
        global label
        # 6 Create frame
        frame = simplegui.create_frame("Pairs", self.WIDTH, self.HEIGHT)
        # 7 Register event handlers for control elements
        frame.set_draw_handler(self.draw)
        frame.add_button("Restart", self.init)
        frame.set_mouseclick_handler(self.mouseclick)
        label=frame.add_label("Moves = 0")
        return

    # This function is executed to start the application
    def main(self):
        """ Class start function """
        self.init_gui()
        # 8 Start frame
        self.init()
        frame.start()
        return 

# always remember to check your completed program against the grading rubric
