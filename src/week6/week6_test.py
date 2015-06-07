#!/usr/bin/env python
# -*- coding: cp1252 -*-

"""
# -*- coding: utf-8 -*-
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
from blackjack import BlackJackGame
from blackjack import Card
from blackjack import Hand
from blackjack import Deck

def dummy(self):
    """ Dummy function for comparison of the return values """
    return

class card_strTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.card = Card("C", "A")

    def testStr(self):
        assert self.card.__str__() == "CA", 'Card.__str__() does not provide the right return value'

class card_getSuitTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.card = Card("C", "A")

    def testGetSuit(self):
        assert self.card.get_suit() == "C", 'Card.get_suit() does not provide the right return value'

class card_getRankTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.card = Card("C", "A")

    def testGetSuit(self):
        assert self.card.get_rank() == "A", 'Card.get_rank() does not provide the right return value'

class card_drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.card = Card("C", "A")

    def tearDown(self):
        """Call after every test case."""

    def testDrawInit(self):
        testCanvas = Canvas()
        pos = [1,1]
        assert self.card.draw(testCanvas, pos) == dummy(self), 'BlackJackGame.draw() does not provide the right return value'

class hand_strTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.hand = Hand()
        self.hand.add_card(Card("C","A"))
        self.hand.add_card(Card("S","2"))
       
    def testStr(self):
        assert self.hand.__str__() == str(['CA', 'S2']), 'Hand.__str__() does not provide the right return value'

class hand_addCardTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.hand = Hand()

    def testAddCard(self):
        assert self.hand.add_card(Card("C","A")) == dummy(self), 'Hand.add_card() does not provide the right return value'

class hand_getValueTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.hand = Hand()

    def testAddCard(self):
        assert self.hand.get_value() == dummy(self), 'Hand.get_value() does not provide the right return value'

class hand_bustedTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.hand = Hand()

    def testAddCard(self):
        assert self.hand.busted() == dummy(self), 'Hand.busted() does not provide the right return value'

class hand_drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.hand = Hand()

    def tearDown(self):
        """Call after every test case."""

    def testDrawInit(self):
        testCanvas = Canvas()
        p = [1,1]
        assert self.hand.draw(testCanvas, p) == dummy(self), 'Hand.draw() does not provide the right return value'

class deck_shuffleTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.deck = Deck()

    def testAddCard(self):
        assert self.deck.shuffle() == dummy(self), 'Deck.shuffle() does not provide the right return value'

class deck_dealCardTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.deck = Deck()

    def testDealCard(self):
        test_card = self.deck.cards[len(self.deck.cards)-1]
        assert self.deck.deal_card() == test_card, 'Deck.deal_card() does not provide the right return value'

class blackJackGame_initTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.blackjack = BlackJackGame()

    def testInit(self):
        assert self.blackjack.init() == dummy(self), 'BlackJackGame.init() does not provide the right return value'

class blackJackGame_dealTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.blackjack = BlackJackGame()
        self.blackjack.init()

    def testDeal(self):
        assert self.blackjack.deal() == dummy(self), 'BlackJackGame.deal() does not provide the right return value'

class blackJackGame_hitTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.blackjack = BlackJackGame()
        self.blackjack.init()

    def testHit(self):
        assert self.blackjack.hit() == dummy(self), 'BlackJackGame.deal() does not provide the right return value'

class blackJackGame_standTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.blackjack = BlackJackGame()
        self.blackjack.init()

    def testHit(self):
        assert self.blackjack.stand() == dummy(self), 'BlackJackGame.deal() does not provide the right return value'

class blackJackGame_drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.blackjack = BlackJackGame()
        self.blackjack.init()

    def tearDown(self):
        """Call after every test case."""

    def testDrawInit(self):
        testCanvas = Canvas()
        assert self.blackjack.draw(testCanvas) == dummy(self), 'BlackJackGame.draw() does not provide the right return value'

class blackJackGame_mainTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.blackjack = BlackJackGame()

    def testMain(self):
        assert self.blackjack.main() == dummy(self), 'BlackJackGame.main() does not provide the right return value'
        
# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

