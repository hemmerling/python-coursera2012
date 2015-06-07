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
#  As I used PyUnit for external testing, some functions 
#  may contain extra code to accompish that,
#  e.g. "apparently unnecessary extra" return values,
#  "apparently unnecessary extra" split of functions,
#  "apparently unnecessary" complicated implementation of code,
#  some few print commands for traditionsl "print on console"
#  testing are in comments.
#
#  And I use a single class to enable testing with PyUnit.
#  Classes are not yet topic of week 3.
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

# 2 Initialize global variables

# Count of 1/10 seconds
tenthseconds = 0

# Shall we count ?
count = False

# Counter for successful number of guesses, total number of guesses
counter_success = 0
counter_tries = 0

class stopWatch():

    # 3 Define global class variables 

    # interval=100  - counts multiples of 1/10 seconds
    # interval=1000 - counts seconds, to make testing easy of the requirement
    #                 "you manage to stop the watch on a whole second",
    #                 as with this setting, you have 1 second to react
    #                 instead of 1/10 second :-).
    interval = 100    
    
    # 4 Helper functions to initialize game   
    def format(self, t):
        """ Define helper function format that converts integer \\
            counting tenths of seconds into formatted string A:BC.D """
        # if the counter exceeds 9:99:9, it starts with 0:00:0 again.
        #result = "0:00:0"
        # Python 2.7.3:
        #result = str(t / 600 % 10 )+":"+str((t / 100 % 6))+str((t / 10 % 10))+":"+str(t % 10)
        #CodeSculptor:
        result = str(t // 600 % 10 )+":"+str((t // 100 % 6))+str((t // 10 % 10))+":"+str(t % 10)
        #print "Format = ", result
        return result

    # 5 Define event handlers for buttons; "Start", "Stop", "Reset"
    def start(self):
        """button that starts the timer """
        global count
        count = True
        return
        
    def stop(self):
        """button that starts the timer """
        global count, tenthseconds, counter_success, counter_tries
        if (count == True):
            if ((tenthseconds % 10) == 0):
                counter_success +=1
            counter_tries +=1    
        count = False
        return 

    def reset(self):
        """button that resets the timer """
        global count, tenthseconds, counter_success, counter_tries
        tenthseconds = 0
        counter_success = 0
        counter_tries = 0
        count = False
        return 
        
    def timer(self):
        """ Define event handler for timer with 0.1 sec interval """
        global tenthseconds, count
        if (count == True):
            tenthseconds += 1
        #print "number = ", tenthseconds, " - ", self.format(tenthseconds)
        return

    def draw(self, canvas):
        """ Define handler to draw on canvas """
        canvas.draw_text(str(counter_success)+"/"+str(counter_tries),[150, 20], 20, "Red")
        #canvas.draw_text(str(tenthseconds),[40, 120], 40, "White")
        canvas.draw_text(self.format(tenthseconds),[40, 120], 40, "White")
        #print self.format(tenthseconds)
        return
    
    # This function is executed to start the application
    def main(self):
        """ Class start function """
        # 6 Create frame
        global frame
        frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
        timer = simplegui.create_timer(self.interval, self.timer)
        # 7 Register event handlers for control elements
        frame.add_button("Start", self.start, 100)
        frame.add_button("Stop", self.stop, 100)
        frame.add_button("Reset", self.reset, 100)
        frame.set_draw_handler(self.draw)
        # 8 Start frame
        frame.start()
        timer.start()
        return 

# always remember to check your completed program against the grading rubric

# 9 run your code

stopWatchGame = stopWatch()
stopWatchGame.main()
