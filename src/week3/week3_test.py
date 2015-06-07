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
#  "Stopwatch: The Game"
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
import simplegui
from stopwatch import stopWatch
from simplegui import Canvas

def dummy(self):
    """ Dummy function for comparison of the return values """
    return
    
class formatTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()
        self.stopWatchGame.main()
     
    def tearDown(self):
        """Call after every test case."""

    def testFormat(self):
        """test case format"""
        assert self.stopWatchGame.format(0) == "0:00:0", "format() does not provide the right response"
        assert self.stopWatchGame.format(11) == "0:01:1", "format() does not provide the right response"
        assert self.stopWatchGame.format(321) == "0:32:1", "format() does not provide the right response"
        assert self.stopWatchGame.format(613) == "1:01:3", "format() does not provide the right response"

class startTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()
        self.stopWatchGame.main()
        
    def tearDown(self):
        """Call after every test case."""

    def testStart(self):
        """test case start"""
        print "start = ", self.stopWatchGame.start()
        assert self.stopWatchGame.start() == dummy(self), "start() does not provide the right response"

class stopTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()
        self.stopWatchGame.main()
     
    def tearDown(self):
        """Call after every test case."""

    def testStop(self):
        """test case stop"""
        assert self.stopWatchGame.stop() == dummy(self), "stop() does not provide the right response"

class resetTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()
        self.stopWatchGame.main()
     
    def tearDown(self):
        """Call after every test case."""

    def testReset(self):
        """test case reset"""
        assert self.stopWatchGame.reset() == dummy(self), "reset() does not provide the right response"

class timerTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()
        self.stopWatchGame.main()
     
    def tearDown(self):
        """Call after every test case."""

    def testTimer(self):
        """test case timer"""
        assert self.stopWatchGame.timer() == dummy(self), "reset() does not provide the right response"

class drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()
        self.stopWatchGame.main()
     
    def tearDown(self):
        """Call after every test case."""

    def testDraw(self):
        """test case timer"""
        self.aCanvas = Canvas()
        assert self.stopWatchGame.draw(self.aCanvas) == dummy(self), "draw() does not provide the right response"

class stopWatchTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.stopWatchGame = stopWatch()

    def tearDown(self):
        """Call after every test case."""

    def testGuessTheNumber(self):
        assert self.stopWatchGame.main() == dummy(self), 'main() does not provide the right return value'
        
# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

