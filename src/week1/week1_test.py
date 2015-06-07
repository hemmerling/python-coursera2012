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

import unittest
import random
from rockpaperscissorslizardspock import rockPaperScissorsLizardSpock

# Initialisation of the random generator
# on my computer, by this, the result of
# random.randrange(self.randomStartValue,self.randomStopValue,1)
# - is always "1" on Python 2.7.3, at first run.
# - is always "2" on ColdeSkulptor, at first run.
# So Python 2.7.3 selects "Spock" at first run, CodeScultor "paper"
myRandomSeed = 3

class numberToNameTest(unittest.TestCase):
    
    def setUp(self):
        """Call before every test case."""
        self.rockPaperScissorsLizardSpock = rockPaperScissorsLizardSpock()

    def tearDown(self):
        """Call after every test case."""

    def testNumberToName(self):
        """Test case NumberToName. note that all test method names must begin with 'test.'"""
        assert self.rockPaperScissorsLizardSpock.number_to_name(0) == "rock", "number_to_name() does not provide the right name"

class numberToNumberTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.rockPaperScissorsLizardSpock = rockPaperScissorsLizardSpock()
     
    def tearDown(self):
        """Call after every test case."""

    def testNameToNumber(self):
        """test case NameToNumber"""
        assert self.rockPaperScissorsLizardSpock.name_to_number("rock") == 0, "name_to_number() does not provide the right number"

class rpslsTest(unittest.TestCase):

    def setUp(self):
        global myRandomSeed
        random.seed(myRandomSeed)
        self.rockPaperScissorsLizardSpock = rockPaperScissorsLizardSpock()

    def tearDown(self):
        """Call after every test case."""

    def testRock(self):
        assert self.rockPaperScissorsLizardSpock.rpsls(self.rockPaperScissorsLizardSpock.rockName) == self.rockPaperScissorsLizardSpock.computerWins, 'rpsls("rock") does not provide the right winner'

    def testRock(self):
        assert self.ockPaperScissorsLizardSpock.rpsls(self.rockPaperScissorsLizardSpock.SpockName) == self.rockPaperScissorsLizardSpock.tieResult, 'rpsls("Spock") does not provide the right winner'

    def testRock(self):
        assert self.rockPaperScissorsLizardSpock.rpsls(self.rockPaperScissorsLizardSpock.paperName) == self.rockPaperScissorsLizardSpock.playerWins, 'rpsls("paper") does not provide the right winner'

    def testRock(self):
        assert self.rockPaperScissorsLizardSpock.rpsls(self.rockPaperScissorsLizardSpock.lizardName) == self.rockPaperScissorsLizardSpock.playerWins, 'rpsls("lizard") does not provide the right winner'

    def testRock(self):
        assert self.rockPaperScissorsLizardSpock.rpsls(self.rockPaperScissorsLizardSpock.scissorsName) == self.rockPaperScissorsLizardSpock.computerWins, 'rpsls("scissors") does not provide the right winner'

# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

