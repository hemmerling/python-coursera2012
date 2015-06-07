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
import unittest
from simplegui import Canvas
from pairs import PairsGame

def dummy(self):
    """ Dummy function for comparison of the return values """
    return

class initCardPoolTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testInitCardPool(self):
        card_pool_static = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
        card_pool = self.pairs.init_card_pool()
        assert card_pool == card_pool_static, 'init_card_pool() does not provide the right return value'

class initCardDeckTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()
        
    def tearDown(self):
        """Call after every test case."""

    def testInitDeckPool(self):
        card_deck_static = [5, 3, 4, 8, 8, 7, 1, 2, 6, 6, 1, 7, 4, 3, 5, 2]
        card_pool = self.pairs.init_card_pool()
        card_deck = self.pairs.init_card_deck(card_pool)
        assert card_deck == card_deck_static, 'init_card_deck() does not provide the right return value'

class initExposed(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()
        
    def tearDown(self):
        """Call after every test case."""

    def testInitExposed(self):
        exposed_static = [False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False]
        exposed = self.pairs.init_exposed(None)
        assert exposed == exposed_static, 'init_exposed() does not provide the right return value'

        exposed_static = [False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False]
        exposed = self.pairs.init_exposed(exposed_static)
        assert exposed == exposed_static, 'init_exposed() does not provide the right return value'

class initFontsize(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()
        
    def tearDown(self):
        """Call after every test case."""

    def testFontSize(self):
        fontsize_static = self.pairs.CARD_HEIGHT/2
        assert self.pairs.fontsize() == fontsize_static, 'fontsize() does not provide the right return value'

class initTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testInit(self):
        assert self.pairs.init() == dummy(self), 'init() does not provide the right return value'

class initCoordinatesOfNumber(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testCoordinatesOfNumber(self):
        self.pairs.init()
        coordinates = [self.pairs.CARD_WIDTH,
                       self.pairs.CARD_HEIGHT+(self.pairs.HEIGHT-self.pairs.CARD_HEIGHT)/4]
        assert self.pairs.coordinates_of_number(1) == coordinates, 'coordinates_of_number() does not provide the right return value'

class initCoordinatesOfNonexposedCardCorner(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testInitCoordinatesOfNonexposedCardCorner(self):
        self.pairs.init()
        coordinates = [self.pairs.CARD_WIDTH,
                       0+self.pairs.HEIGHT/4]
        assert self.pairs.coordinates_of_nonexposed_card_corner(1, 0) == coordinates, 'coordinates_of_nonexposed_card_corner does not provide the right return value'

class drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testDrawInit(self):
        self.pairs.init()
        testCanvas = Canvas()
        assert self.pairs.draw(testCanvas) == dummy(self), 'draw() does not provide the right return value'

class mouseclickTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testMouseclickInit(self):
        self.pairs.init_gui()
        self.pairs.init()
        pos = [self.pairs.CARD_WIDTH/2, self.pairs.HEIGHT/4+self.pairs.CARD_HEIGHT/2]
        card_index = 1
        card_value = 7
        assert self.pairs.mouseclick(pos) == (0, 5), 'mouseclick() does not provide the right return value'

class pairsTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pairs = PairsGame()

    def tearDown(self):
        """Call after every test case."""

    def testGuessTheNumber(self):
        assert self.pairs.main() == dummy(self), 'main() does not provide the right return value'
        
# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

