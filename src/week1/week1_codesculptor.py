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
#  "Rock-paper-scissors-lizard-Spock"
#  for the Coursera course
#  "An Introduction to Interactive Programming in Python"
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

import random

# Initialisation of the random generator
# on my computer, by this, the result of
# random.randrange(self.randomStartValue,self.randomStopValue,1)
# - is always "1" on Python 2.7.3, at first run.
# - is always "2" on ColdeSkulptor, at first run.
# So Python 2.7.3 selects "Spock" at first run, CodeScultor "paper"
myRandomSeed = 3

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

rockName = "rock"
spockName = "Spock"
paperName = "paper"
lizardName = "lizard"
scissorsName = "scissors"
notAnItemName = "None"
computerWins = "Computer wins!"
playerWins = "Player wins!"
tieResult = "Player and computer tie!"

rockNumber = 0
spockNumber = 1
paperNumber = 2
lizardNumber = 3
scissorsNumber = 4
notAnItemNumber = -1
randomStartValue = rockNumber
randomStopValue = scissorsNumber+1

# helper functions

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == rockNumber: return rockName
    if number == spockNumber: return spockName
    if number == paperNumber: return paperName
    if number == lizardNumber: return lizardName
    if number == scissorsNumber: return scissorsName     
    return notAnItemName
    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == rockName: return rockNumber
    if name == spockName: return spockNumber
    if name == paperName: return paperNumber
    if name == lizardName: return lizardNumber
    if name == scissorsName: return scissorsNumber     
    return notAnItemNumber

def rpsls(name): 
    global myRandomSeed
    ##random.seed(myRandomSeed)
    # convert name to playerNumber using name_toNumber
    player_number = name_to_number(name)
    # compute random guess for compNumber using random.randrange()
    compNumber = random.randrange(randomStartValue,randomStopValue,1)
    # compute difference of playerNumber and compNumber modulo five
    difference = ( player_number - compNumber ) % 5
    # use if/elif/else to determine winner
    # each choice wins agains the preceding two choices ( difference = 1, 2 )
    # and loses against the following two choices ( difference = 3, 4 )
    # or both player and computer answer the same = tie result ( difference = 0 )
    if difference>2: resultMessage = computerWins
    elif difference>0: resultMessage = playerWins
    else: resultMessage = resultMessage = tieResult
    # convert compNumber to name using number_to_name
    compName = number_to_name(compNumber)
    # print results
    # 1. print a blank line.
    print
    # 2. print out the player's choice.
    print "Player chooses ", name
    # 3. print out the computer's choice.
    print "Computer chooses ", compName
    # 4. print out the winner. 
    print resultMessage
    ## print "player, computer, difference =", player_number, compNumber, difference
    return resultMessage
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
