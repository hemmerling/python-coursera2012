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
#  "Guess The Number"
#  for the Coursera course
#  "An Introduction to Interactive Programming in Python"
#
#  Help for the evaluation:
#  If you enter "Cheat", the computer tells you the secret number
#  at any time, and this does you not even cost you a try :-).
#  E.g. so You can easily check what happens if there is just 1 try left,
#  and you either guess right or wrong.
#
#  Input will come from buttons and an input field
#  all output for the game will be printed in the console
#
#  As I used PyUnit for external testing, some functions 
#  may contain extra code to accompish that,
#  e.g. "apparently unnecessary extra" return values,
#  "apparently unnecessary extra" split of functions,
#  "apparently unnecessary" complicated implementation of code,
#  some few code just used outside CodeSculptor ist in comments.
#
#  And I use a single class to enable testing with PyUnit.
#  Classes are not yet topic of week 2.
#
#  I also added some error-handling to catch faulty input,
#  which is not yet topic of week 2
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
import math

# 2 Initialize global variables

# Initialisation of the random generator
# on my computer, for use with PyUnit
# By this, the result of
# random.randrange(self.0,100,1)
# - is always "23" on Python 2.7.3, at first run.
# - is always "55" on ColdeSkulptor, at first run.
# random.randrange(self.0,1000,1)
# - is always "237" on Python 2.7.3, at first run.
# - is always "550" on ColdeSkulptor, at first run.
myRandomSeed = 3

class guessTheNumber():

    # 2 Initialize global class variables
    newgame_message = "Please guess a number in the range [0, %d)"
    correctguess_message = "Correct!"
    num_range = 100
    remaining_guesses = 5 # not seven, to enable some useful PyUnit testing
    secret_number = 0
    
    # 3 Helper functions to initialize game   
    def set_guesses(self, guesses):
        """ Initialize number of guesses"""
        # Global remaining_guesses
        self.remaining_guesses = guesses
        return guesses

    def set_range(self, range):
        """ Initialize range"""
        # Global num_range
        self.num_range = range
        return range

    def set_secret_number(self):
        """ Initialize secret number"""
        # Global secret_number
        self.secret_number = random.randrange(0,self.num_range,1)
        return self.secret_number

    def calculate_number_of_guesses(self, range):
        """ Calculate the necessary number of guesses """
        # Python 2.7.3: math.ceil() is a float
        # CodeSculptor: math.ceil() is an integer
        return int(math.ceil(math.log(range,2)))
    
    def init(self, range):
        """ Initialization """
        print
        print
        print "Let's play the game 'Guess The Number'!"
        print
        print "You may restart by pressing the 'Range is..' buttons"
        print self.newgame_message % (self.set_range(range)) 
        calculated_number_of_guesses = self.calculate_number_of_guesses(range)
        print "You may guess the number with %d tries or less" % (calculated_number_of_guesses)
        self.set_guesses(calculated_number_of_guesses)
        self.set_secret_number()
        return self.newgame_message % (self.set_range(range)) 

    def out_of_range_check(self, guess, range):
        """ Check if the input is out of range """
        if ((guess<0) or (guess>=range)):
            return "Input is out of range!"
        else:
            return guess
        
    def verify_input(self, guess, range):
        """ Verify player's input """
        # Catch faulty input, this is not topic of week 2
        try:
            result = int(guess)
        except:
            result = "Wrong input!"
            # CodeSkulptor does not accept references ( = e.g. writing
            # to global variables and class variables ) here...
            return result
        return self.out_of_range_check(result, range)
    
    def process_player_input(self,guess):
        """ Process player's input, return appropriate message """
        # Step 1 - Catch faulty input, this is not topic of week 2

        # Tell the player the secret number :-)
        if (guess == "Cheat"):
            return "Secret number = %d" % (self.secret_number)
        
        # Step 2 - Verify player's input.
        user_input = self.verify_input(guess, self.num_range)
        if (type(user_input) != type(0)):
            # Verify_input() detected faulty input
            # Let's leave here with the error message
            return user_input

        # Decrease the number of still available tries
        if (self.remaining_guesses>0):
            self.remaining_guesses -= 1
        print "Remaining number of tries = ", self.remaining_guesses
        
        # Step 3 - Give the player a hint for next guess
        if ((user_input > self.secret_number) and (self.remaining_guesses > 0)):
            # Give a hint just if the player has another try
            result_message = "Lower!"
        elif ((user_input < self.secret_number) and (self.remaining_guesses > 0)):
            # Give a hint just if the player has another try
            result_message = "Higher!"
        elif (user_input == self.secret_number):
            result_message = self.correctguess_message
        else:
            # As the guess was wrong and there is no further try anymore,
            # tell the player that he/she lost
            result_message = "You tried too often than necessary, You lost!"
        return result_message
        
    def get_input(self, guess):
        """ Main game logic goes here """
        print
        print "The player guessed = ", guess
        result = self.process_player_input(guess)
        print result
        if ((self.remaining_guesses == 0) or ( result == self.correctguess_message)):
            # Start a new game, with same range
            self.init(self.num_range)
        return result

    # 4 Define event handlers for control panel
    def range100(self):
        """button that changes range to range [0,100) and restarts """
        return self.init(100)
        
    def range1000(self):
        """ Button that changes range to range [0,1000) and restarts """
        return self.init(1000)
            
    # This function is executed to start the application
    def main(self):
        """ Class start function """
        # Let's start with the range 0,100
        self.range100()
        # 5 Create frame
        global frame
        frame = simplegui.create_frame("Guess the number", 200, 200)
        # 6 Register event handlers for control elements
        frame.add_button("Range is [0,100)", self.range100, 200)
        frame.add_button("Range is [0,1000)", self.range1000, 200)
        frame.add_input("Enter a guess", self.get_input, 200)
        # 7 Start frame
        frame.start()
        return self.secret_number
    
# always remember to check your completed program against the grading rubric

# This statement must be just enabled for testing
# by the developer, not by the evaluation tester.
# By this the sequence of random number is repeatable..
##random.seed(myRandomSeed)       

gTN = guessTheNumber()
gTN.main()
