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

# import modules
import random
import unittest
import random
from guessthenumber import myRandomSeed
from guessthenumber import guessTheNumber

class setGuessesTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.gTN = guessTheNumber()
     
    def tearDown(self):
        """Call after every test case."""

    def testInitGuesses(self):
        """test case set_guesses"""
        self.gTN.set_guesses(7)
        assert self.gTN.set_guesses(7) == self.gTN.remaining_guesses, "set_guesses() does not provide the right number"
        assert self.gTN.set_guesses(7) == 7, "set_guesses() does not provide the right number"
        assert self.gTN.set_guesses(7) != 8, "set_guesses() does not provide the right number"

class rangeTest(unittest.TestCase):

    const_newgame_message100 = "Please guess a number in the range [0, 100)"
    const_newgame_message1000 = "Please guess a number in the range [0, 1000)"
    
    def setUp(self):
        """Call before every test case."""
        self.gTN = guessTheNumber()

    def tearDown(self):
        """Call after every test case."""

    def testRange(self):
        """Test case range100, range1000. note that all test method names must begin with 'test.'"""
        assert self.gTN.range100() == self.const_newgame_message100, "range100 does not provide the right string"
        assert self.gTN.range1000() == self.const_newgame_message1000, "range1000 does not provide the right string"
        assert self.gTN.range100() != self.const_newgame_message1000, "range100 does not provide the right string"
        assert self.gTN.range1000() != self.const_newgame_message100, "range1000 does not provide the right string"
        pass
    
class setRangeTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.gTN = guessTheNumber()
     
    def tearDown(self):
        """Call after every test case."""

    def testSetRange(self):
        """test case set_range"""
        assert self.gTN.set_range(100) == 100, "set_range() does not provide the right number"
        assert self.gTN.set_range(1000) == 1000, "set_range() does not provide the right number"
        assert self.gTN.set_range(100) != 1000, "set_range() does not provide the right number"
        assert self.gTN.set_range(1000) != 100, "set_range() does not provide the right number"

class setSecretNumberTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.gTN = guessTheNumber()
     
    def tearDown(self):
        """Call after every test case."""

    def testSetSecretNumber(self):
        """test case set_secret_number"""
        global myRandomSeed
        random.seed(myRandomSeed)
        secret_number = self.gTN.set_secret_number()
        assert secret_number == 23, "set_secret_number() does not provide the right number"
        assert self.gTN.secret_number == 23, "set_secret_number() does not provide the right number"
        
class outOfRangeCheckTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.gTN = guessTheNumber()
     
    def tearDown(self):
        """Call after every test case."""

    def testOutOfRangeCheck(self):
        """test case out_of_range_check """
        assert self.gTN.out_of_range_check(99,100) == 99, "out_of_range_check() does not provide the right number"
        assert self.gTN.out_of_range_check(100,100) == "Input is out of range!", "out_of_range_check() does not provide a proper return answer"
        assert self.gTN.out_of_range_check(-1,100) == "Input is out of range!", "out_of_range_check() does not provide a proper return answer"

        assert self.gTN.out_of_range_check(999,1000) == 999, "out_of_range_check() does not provide the right number"
        assert self.gTN.out_of_range_check(1000,1000) == "Input is out of range!", "out_of_range_check() does not provide the right return answer"
        assert self.gTN.out_of_range_check(-1,1000) == "Input is out of range!", "out_of_range_check() does not provide the right return answer"

class verifyInputTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.gTN = guessTheNumber()
     
    def tearDown(self):
        """Call after every test case."""

    def testVerifyInput(self):
        """test case verify_input """
        interactive_input = raw_input("Guess ( Please enter 55 ) = ")
        guess = self.gTN.verify_input(interactive_input, 100)
        assert guess == 55, "get_input() does not provide the right number"

class processPlayerInputTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        global myRandomSeed
        random.seed(myRandomSeed)
        self.gTN = guessTheNumber()
        self.gTN.main()
        
    def tearDown(self):
        """Call after every test case."""

    def testProcessPlayerInput(self):
        """test case process_player_input"""
        print ("das ist der Cheat = ", self.gTN.process_player_input("Cheat"))
        assert self.gTN.process_player_input("Cheat") == "Secret number = 23", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(50) == "Lower!", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(25) == "Lower!", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(13) == "Higher!", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(17) == "Higher!", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(20) == "Higher!", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(22) == "Higher!", "process_player_input() does not provide the right answer"
        assert self.gTN.process_player_input(23) == "Correct!", "process_player_input() does not provide the right answer"

class guessTheNumberTest(unittest.TestCase):

    def setUp(self):
        global myRandomSeed
        random.seed(myRandomSeed)
        self.gTN = guessTheNumber()

    def tearDown(self):
        """Call after every test case."""

    def testGuessTheNumber(self):
        assert self.gTN.main() == self.gTN.secret_number, 'main() does not provide the right secret number'
        
# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

