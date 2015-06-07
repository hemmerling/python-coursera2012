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
#  As I used PyUnit for external testing, some functions 
#  may contain extra code to accompish that,
#  e.g. "apparently unnecessary extra" return values,
#  "apparently unnecessary extra" split of functions,
#  "apparently unnecessary" complicated implementation of code,
#  some few print commands for traditionsl "f on console"
#  testing are in comments.
#
#  And I use a single class to enable testing with PyUnit.
#  Classes are not yet topic of week 4.
#
#  In opposite to week 1-3, according to Joe's video, the game starts 
#  automatically at start of code execution. I.e. the game does not wait for 
#  a first time "Restart" keypress.
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
DEFAULT_VELOCITY_PADDLE = 0.0
    
class PongGame():

    # 3 initialize class globals - pos and vel encode vertical info for paddles
    WIDTH = 600
    HEIGHT = 400       
    BALL_RADIUS = 20
    PAD_WIDTH = 8
    PAD_HEIGHT = 80
    HALF_PAD_WIDTH = PAD_WIDTH / 2
    HALF_PAD_HEIGHT = PAD_HEIGHT / 2

    # default velocity, 
    # default acceleration  ( addition, not multiplication )
    DEFAULT_VELOCITY_BALL = 5.0
    DELTA_VELOCITY_BALL = 5.0
    DELTA_VELOCITY_PADDLE = 20.0
    
    paddle1_pos = int(HEIGHT/2)
    paddle2_pos = int(HEIGHT/2)
    paddle1_vel = DEFAULT_VELOCITY_PADDLE
    paddle2_vel = DEFAULT_VELOCITY_PADDLE
    
    # Score for the players
    score1 = 0
    score2 = 0
    
    # ball position and velocity
    global_ball_pos  = [0, 0]
    global_ball_vel  = [0, 0]

    # factor is increased by 10% each time you hit the paddle
    speed_factor = 1.0
    # 4 Helper functions to initialize game   

    # helper function that spawns a ball, returns a position vector and a velocity vector
    # if right is True, spawn to the right, else spawn to the left
    def ball_init(self, right):
        """ Initialize the Ball with coordinates and velocity """
        # class global ball_pos, ball_vel # these are vectors stored as lists
        self.global_ball_pos = [300,200]
        #
        # Requirement 11 "To moderately increase the difficulty of your game,
        # increase the velocity of the ball by 10% each time
        # it strikes a paddle"
        # Developer's decision: With new ball, speed will be slowed
        # down again, as else the game becomes unplayable and does not
        # look well if there speed starts with factor 2,3,4..
        # 
        self.speed_factor = 1.0 
        # suggested settings for code development
        #vel_x = self.DEFAULT_VELOCITY_BALL
        #vel_y = self.DEFAULT_VELOCITY_BALL
        # suggested settings by the course instructions:
        #vel_x = int ((self.speed_factor * random.randrange(120,140))//60 )
        #vel_y = int ((self.speed_factor * random.randrange(60,180))//60 )
        # my settings
        # Make ball faster, after paddle hits
        vel_x = int ((self.speed_factor * random.randrange(200,500))//60 )
        vel_y = int ((self.speed_factor * random.randrange(200,500))//60 )
        if (right):
            self.global_ball_vel = [vel_x, -vel_y]
        else:
            self.global_ball_vel = [-vel_x, -vel_y]            
        return self.global_ball_pos, self.global_ball_vel
    
    def vertical_update_ball(self, ball_pos):
        """ Update vertical ball position """
        updated_ball_pos = ball_pos
        # Update vertical position
        if (updated_ball_pos[1] <= self.BALL_RADIUS):
            # The ball is at the lower edge
            # For bouncing: Change direction of movement, before update
            self.global_ball_vel[1]= - self.global_ball_vel[1]
        else:
            if ( updated_ball_pos[1] >= self.HEIGHT - self.BALL_RADIUS ):
                # The ball is at the lower edge
                # For bouncing: Change direction of movement, before update
                self.global_ball_vel[1] = - self.global_ball_vel[1]
            else:    
                # Ball is not too high and not too low
                # Just update vertical position
                pass
        # update anyhow 
        # by this the ball gets out of the limits,
        # so that out-of-limits is not detected with next cycle
        # and we must not check the direction of the ball velocity
        updated_ball_pos[1] +=self.global_ball_vel[1]
        return updated_ball_pos
   
    def horizontal_update_ball(self, ball_pos):
        """ Update horizontal ball position """
        global speed_factor
        updated_ball_pos = ball_pos
        if (updated_ball_pos[0] <= self.PAD_WIDTH + self.BALL_RADIUS):
            # The ball is at the left edge.
            # For bouncing: Change direction of movement, before update
            self.global_ball_vel[0]= - self.global_ball_vel[0]
            # Calculation without making use of geometric distance formula: 
            # Does the ball hit the paddle?
            #
            # If at the moment where the ball touches the gutter,
            # and if the vertical distance is as big as or bigger as the 
            # "sum of ball radius and half of the paddle", 
            # the ball would not touch the paddle when passing by...
            #
            if  (math.abs(updated_ball_pos[1]-self.paddle1_pos) >= (self.HALF_PAD_HEIGHT+self.BALL_RADIUS)):
                self.score2 += 1
                self.ball_init(True)
            else:
                # Requirement 11 "To moderately increase the difficulty of your game,
                # increase the velocity of the ball by 10% each time
                # it strikes a paddle"
                self.speed_factor *= 1.1 
        else:
            if (updated_ball_pos[0] >= self.WIDTH - self.PAD_WIDTH - self.BALL_RADIUS):
                # The ball is at the right edge.
                # For bouncing: Change direction of movement, before update
                self.global_ball_vel[0]= - self.global_ball_vel[0]
                # Calculation without making use of geometric distance formula: 
                # Does the ball hit the paddle?
                #
                # If at the moment where the ball touches the gutter,
                # and if the vertical distance is as big as or bigger as the 
                # "sum of ball radius and half of the paddle", 
                # the ball would not touch the paddle when passing by...
                #
                if  (math.abs(updated_ball_pos[1]-self.paddle2_pos) >= (self.HALF_PAD_HEIGHT+self.BALL_RADIUS)):
                    self.score1 += 1
                    self.ball_init(False)
                else:
                    # Requirement 11 "To moderately increase the difficulty of your game,
                    # increase the velocity of the ball by 10% each time
                    # it strikes a paddle"
                    self.speed_factor *= 1.1 
            else:
                # Ball is not too much right or left
                # Just update horizontal position
                pass
        # update anyhow 
        # by this the ball gets out of the limits,
        # so that out-of-limits is not detected with next cycle
        # and we must not check the direction of the ball velocity
        updated_ball_pos[0] +=self.global_ball_vel[0]
        return updated_ball_pos

    def update_paddle(self, paddle_pos, paddle_vel):
        """ Update paddle position """
        updated_paddle_pos = paddle_pos
        if (paddle_vel>0):
            if (updated_paddle_pos >= self.HEIGHT - self.HALF_PAD_HEIGHT):
                # The paddle is at the top
                pass
            else:
                updated_paddle_pos +=paddle_vel
        if (paddle_vel<0):
            if (updated_paddle_pos <= self.HALF_PAD_HEIGHT):
                # The paddle is at the top
                pass
            else:
                updated_paddle_pos +=paddle_vel
        return updated_paddle_pos

    def reset_game(self):
        """ Reset the game. Do not change paddels """
        self.score1 = 0
        self.score2 = 0
        self.speed_factor = 1.0
        # Initialize the ball..
        self.ball_init(True)
        return

    # 5 Define event handlers
    def init(self):
        """ Initialize """
        global DEFAULT_VELOCITY_PADDLE
        # class global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
        # class global score1, score2  # these are ints
        self.paddle1_pos = int(self.HEIGHT/2)
        self.paddle2_pos = int(self.HEIGHT/2)
        self.paddle1_vel = DEFAULT_VELOCITY_PADDLE
        self.paddle2_vel = DEFAULT_VELOCITY_PADDLE
        self.reset_game()
        return self.paddle1_pos, self.paddle2_pos, self.paddle1_vel, self.paddle2_vel, self.score1, self.score2

    def update_ball(self, ball_pos):
        """ Update ball position """
        # Vertical ball position update
        updated_ball_pos = self.vertical_update_ball(ball_pos)
        # Horizontal ball position update
        updated_ball_pos = self.horizontal_update_ball(updated_ball_pos)        
        return updated_ball_pos
    
    def draw_ball(self, c2, ball_pos, color):
        """ Draw or undraw ball """
        center_point = ball_pos
        radius = self.BALL_RADIUS
        line_width = 1
        line_color = color
        fill_color = color
        c2.draw_circle(center_point, radius, line_width, line_color, fill_color)
        return center_point, radius, line_color, fill_color
    
    def draw(self, c):
        """ Draw """
        # class global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        # update paddle's vertical position, keep paddle on the screen
        new_paddle1_pos = self.update_paddle(self.paddle1_pos, self.paddle1_vel)
        new_paddle2_pos = self.update_paddle(self.paddle2_pos, self.paddle2_vel)
        
        # draw mid line and gutters
        c.draw_line([self.WIDTH / 2, 0],[self.WIDTH / 2, self.HEIGHT], 1, "White")
        c.draw_line([self.PAD_WIDTH, 0],[self.PAD_WIDTH, self.HEIGHT], 1, "White")
        c.draw_line([self.WIDTH - self.PAD_WIDTH, 0],[self.WIDTH - self.PAD_WIDTH, self.HEIGHT], 1, "White")
    
        # draw paddles           
        # Top right corner = (a, b)
        width = self.PAD_WIDTH # For squares, width = height
        height = self.PAD_HEIGHT
        a = 0
        b = self.paddle1_pos - self.HALF_PAD_HEIGHT
        c.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 1, "Black", "Black")        
        self.paddle1_pos = new_paddle1_pos
        b = self.paddle1_pos - self.HALF_PAD_HEIGHT
        c.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 1, "White", "White")        
        
        a = self.WIDTH - self.PAD_WIDTH
        b = self.paddle2_pos - self.HALF_PAD_HEIGHT
        c.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 1, "Black", "Black")        
        self.paddle2_pos = new_paddle2_pos
        b = self.paddle2_pos - self.HALF_PAD_HEIGHT
        c.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 1, "White", "White")        
        
        # update ball
        new_ball_pos = self.update_ball(self.global_ball_pos)
        
        # draw ball and scores
        self.draw_ball(c, self.global_ball_pos, "Black")
        ball_pos = new_ball_pos
        self.draw_ball(c, self.global_ball_pos, "White")
        c.draw_text(str(self.score1), (self.WIDTH / 2 - 2*50, self.HEIGHT / 4), 50, "White")
        c.draw_text(str(self.score2), (self.WIDTH / 2 + 50, self.HEIGHT / 4), 50, "White")
        return
        
    def keydown(self, key):
        """ Key pressed """
        # class global paddle1_vel, paddle2_vel
        if (key == 87): # key "w"
            self.paddle1_vel = -self.DELTA_VELOCITY_PADDLE
        if (key == 38): # key "arrow up"
            self.paddle2_vel = -self.DELTA_VELOCITY_PADDLE
        if (key == 83): # key "s"
            self.paddle1_vel = self.DELTA_VELOCITY_PADDLE
        if (key == 40): # key "arrow down"
            self.paddle2_vel = self.DELTA_VELOCITY_PADDLE
        return self.paddle1_vel, self.paddle2_vel
   
    def keyup(self, key):
        """ Key released """
        # class global paddle1_vel, paddle2_vel
        if (key == 87): # key "w"
            self.paddle1_vel = DEFAULT_VELOCITY_PADDLE
        if (key == 38): # key "arrow up"
            self.paddle2_vel = DEFAULT_VELOCITY_PADDLE
        if (key == 83): # key "s"
            self.paddle1_vel = DEFAULT_VELOCITY_PADDLE
        if (key == 40): # key "arrow down"
            self.paddle2_vel = DEFAULT_VELOCITY_PADDLE
        return self.paddle1_vel, self.paddle2_vel
    
    # This function is executed to start the application
    def main(self):
        """ Class start function """
        # 6 Create frame
        global frame
        frame = simplegui.create_frame("Pong", self.WIDTH, self.HEIGHT)
        # 7 Register event handlers for control elements
        frame.set_draw_handler(self.draw)
        frame.set_keydown_handler(self.keydown)
        frame.set_keyup_handler(self.keyup)
        frame.add_button("Restart", self.reset_game, 100)
        # 8 Start frame
        self.init()
        frame.start()
        return 

# always remember to check your completed program against the grading rubric
