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

# 1 import modules
import random
from guessthenumber import myRandomSeed
from guessthenumber import guessTheNumber

# 8 run your code

# This statement must be just enabled for testing
# by the developer, not by the evaluation tester.
# By this the sequence of random number is repeatable..
random.seed(myRandomSeed)       

gTN = guessTheNumber()
gTN.main()
gTN.get_input("Cheat")
gTN.get_input(50)
gTN.get_input(25)
gTN.get_input(13)
gTN.get_input(17)
gTN.get_input(20)
gTN.get_input(22)
gTN.get_input(23)




