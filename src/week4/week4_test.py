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
#  "Pong"
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
from pong import PongGame

def dummy(self):
    """ Dummy function for comparison of the return values """
    return

class ballInitTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pong = PongGame()

    def tearDown(self):
        """Call after every test case."""

    def testBallInit(self):
        right = None
        ball_pos = [300,200]
        ball_vel = [5, 5]
        assert self.pong.ball_init(right) == (ball_pos, ball_vel), 'ball_init() does not provide the right return value'

class initTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pong = PongGame()

    def tearDown(self):
        """Call after every test case."""

    def testInit(self):
        test_paddle1_pos = 200.0
        test_paddle2_pos = 150.0
        test_paddle1_vel = 5.0
        test_paddle2_vel = 5.0
        test_score1 = 0
        test_score2 = 0
        assert self.pong.init() == (test_paddle1_pos, test_paddle2_pos, test_paddle1_vel, test_paddle2_vel, test_score1, test_score2), 'init() does not provide the right return value'

class drawBallTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pong = PongGame()
        self.pong.init()

    def tearDown(self):
        """Call after every test case."""

    def testDrawBall(self):
        self.aCanvas = Canvas()
        test_paddle1_pos = 200.0
        test_paddle2_pos = 150.0
        test_paddle1_vel = self.pong.DEFAULT_VELOCITY
        test_paddle2_vel = self.pong.DEFAULT_VELOCITY
        ball_radius = self.pong.BALL_RADIUS
        ball_pos = [300,200]
        color = "Black"
        assert self.pong.draw_ball(self.aCanvas, ball_pos, color) == (ball_pos, ball_radius, color, color), 'draw_ball() does not provide the right return value'
        color = "White"
        assert self.pong.draw_ball(self.aCanvas, ball_pos, color) == (ball_pos, ball_radius, color, color), 'draw_ball() does not provide the right return value'
        
class keyDownTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pong = PongGame()
        self.pong.init()

    def tearDown(self):
        """Call after every test case."""

    def testKeyDown(self):
        test_paddle1_vel = self.pong.paddle1_vel+self.pong.DELTA_VELOCITY
        test_paddle2_vel = self.pong.paddle2_vel
        assert self.pong.keydown("down") == (test_paddle1_vel, test_paddle2_vel), 'key_down() #1 does not provide the right return value'
        test_paddle1_vel = self.pong.paddle1_vel
        test_paddle2_vel = self.pong.paddle2_vel+self.pong.DELTA_VELOCITY
        assert self.pong.keydown("x") == (test_paddle1_vel, test_paddle2_vel), 'key_down() #2 does not provide the right return value'
        return
        
class keyUpTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pong = PongGame()
        self.pong.init()

    def tearDown(self):
        """Call after every test case."""

    def testKeyUp(self):
        test_paddle1_vel = self.pong.paddle1_vel-self.pong.DELTA_VELOCITY
        test_paddle2_vel = self.pong.paddle2_vel
        assert self.pong.keyup("up") == (test_paddle1_vel, test_paddle2_vel), 'key_up() #1 does not provide the right return value'    
        test_paddle1_vel = self.pong.paddle1_vel
        test_paddle2_vel = self.pong.paddle2_vel-self.pong.DELTA_VELOCITY
        assert self.pong.keyup("e") == (test_paddle1_vel, test_paddle2_vel), 'key_up() #2 does not provide the right return value'

class pongTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pong = PongGame()

    def tearDown(self):
        """Call after every test case."""

    def testGuessTheNumber(self):
        assert self.pong.main() == dummy(self), 'main() does not provide the right return value'
        
# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

