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
#  "Asteroids"
#  for the Coursera course
#  "An Introduction to Interactive Programming in Python"
#
#  My game displays the highscore of last game,
#  as long as no new game is started :-).
#
#  As I used PyUnit for external testing, some functions
#  may contain extra code to accompish that,
#  e.g. "apparently unnecessary extra" return values,
#  "apparently unnecessary extra" split of functions,
#  "apparently unnecessary" complicated implementation of code,
#  some few print commands for traditional "print on console"
#  testing are in comments.
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
import math
import random

# 2 Initialize global variables
WIDTH = 800
HEIGHT = 600
NUMBER_OF_LIVES = 3

score = 0
lives = NUMBER_OF_LIVES
time = 0

started = False

# Initialisation of the random generator
# on my computer, by this, the result of
# random.randrange(self.randomStartValue,self.randomStopValue,1)
# - is always "1" on Python 2.7.3, at first run.
# - is always "2" on ColdeSkulptor, at first run.
myRandomSeed = 3

# Global objects
ship_image = None

# Global class objects
my_ship = None
#a_rock = None
a_missile = None

# Collection of rocks and missiles
rock_group = None
missile_group = None

# define classes

class ImageInfo:
    """ Collection of informations about the images"""
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# Ship class
class Ship:
    
    # The timing for the delay the thrust sound plays
    # after keyup of the thrust key
    # is suitable for Dell VOSTRO 1000 notebooks
    THRUST_SOUND_DELAY = 20
    
    # Acceleration by pressing the thrust key, for one period
    THRUST = 1
    # Friction
    FRICTION = 0.1
    # Speed of the missile
    MISSILE_SPEED = 20
    
    """ Ship class """
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        # get lifespam of object
        self.lifespan =  info.get_lifespan()
        self.thrust_lifespan = 0 # might alternatively be an image property...
    
    def draw(self,canvas):
        global ship_thrust_sound, started
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        image_center_draw = self.image_center
        if (self.thrust):
            image_center_draw = [self.image_center[0] + self.image_size[0], self.image_center[1]]
        else:
            image_center_draw = [self.image_center[0], self.image_center[1]]
        canvas.draw_image(self.image, image_center_draw, self.image_size, self.pos, self.image_size, self.angle)

        # Just for sound
        if (self.thrust):
            self.thrust_lifespan = self.THRUST_SOUND_DELAY
        if (self.thrust_lifespan>0):
            self.thrust_lifespan -=1
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
        return

    # helper functions to handle transformations
    def angle_to_vector(self, ang):
        return [math.cos(ang), math.sin(ang)]
    
    def update(self):
        self.angle += self.angle_vel
        # Speed update
        # Slowdown due to friction ( in Space :-) )!
        if (self.thrust):
            self.vel = [self.vel[0]*(1-self.FRICTION)+self.THRUST*self.angle_to_vector(self.angle)[0], \
                        self.vel[1]*(1-self.FRICTION)+self.THRUST*self.angle_to_vector(self.angle)[1]]
        else:
            self.vel = [self.vel[0]*(1-self.FRICTION), self.vel[1]*(1-self.FRICTION)]
        # Position update
        self.pos = [(self.pos[0]+self.vel[0])%WIDTH, (self.pos[1]+self.vel[1])%HEIGHT]
        return

    def shoot(self):
        global missile_group
        #global a_missile
        #a_missile = self.generate_dynamic_missile()
        missile_group.append(self.generate_dynamic_missile())
        return

    # Generation of a missile with dymamic parameters	
    def generate_dynamic_missile(self):
        global missile_image1, missile_image2, missile_image3, \
               missile_info, missile_sound
        newmissile_pos = [self.pos[0]+self.angle_to_vector(self.angle)[0]*self.image_size[0]/2, \
                          self.pos[1]+self.angle_to_vector(self.angle)[1]*self.image_size[1]/2]
        newmissile_vel = [self.vel[0]+self.MISSILE_SPEED*self.angle_to_vector(self.angle)[0], \
                          self.vel[1]+self.MISSILE_SPEED*self.angle_to_vector(self.angle)[1]]
        newmissile_ang = self.angle
        newmissile_ang_vel = 0
        # Random selection of the kind of missile
        #newmissile_image = missile_image1
        newmissile_image_dic = { 0: missile_image1, 1:missile_image2, 2:missile_image3}
        newmissile_image = newmissile_image_dic[random.randrange(0, 3, 1)]
        newmissile_info = missile_info
        newmissile_sound = missile_sound
        return Sprite( newmissile_pos, newmissile_vel, newmissile_ang, newmissile_ang_vel, \
                            newmissile_image, newmissile_info, newmissile_sound)        

    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius

# Sprite class
class Sprite:
    """ Sprite Class """
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.animated = info.get_animated()
        self.lifespan = info.get_lifespan()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        return
    
    def update(self):
        self.age += 1
        self.angle += self.angle_vel
        self.pos = [(self.pos[0]+self.vel[0])%WIDTH, (self.pos[1]+self.vel[1])%HEIGHT]
        return self.age < self.lifespan

    # helper functions to handle transformations
    def dist(self, p,q):
       return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

    def collide(self, other_object):
        """Check if 2 objects collide"""
        #collision = False
        distance = self.dist(self.get_position(), other_object.get_position())
        collision = (distance < ( self.get_radius() + other_object.get_radius()))
        #if collision:
        #    print "Kollision!"
        return collision
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius

class AsteroidsGame():
    """ Implementation of the game Asteroids """

    # 3 initialize class globals
    SHIP_ANGLE_VELOCITY = 0.1

    ROCK_MINSPEED = -5
    ROCK_MAXSPEED = 5
    
    ROCK_MIN_ANGVEL = -3
    ROCK_MAX_ANGVEL = 3
    
    # 4 Helper functions to initialize game
    def init(self):
        global debris_info, nebula_info, splash_info,             \
               ship_info, missile_info, asteroid_info,            \
               explosion_info
        global debris_image1, debris_image2, debris_image3,       \
               debris_image4, debris_image5, debris_image6,       \
               debris_image7, debris_image8, debris_image8,       \
               debris_image9,                                     \
               nebula_image1, nebula_image2,                	  \
               splash_image, ship_image,                          \
               missile_image1, missile_image2, missile_image3,    \
               asteroid_image1, asteroid_image2, asteroid_image3, \
               explosion_image
        global soundtrack, missile_sound, ship_thrust_sound,      \
               explosion_sound
        global my_ship, a_rock, a_missile
        global rock_group, missile_group

        global myRandomSeed
        global started, score, lives
                
        random.seed(myRandomSeed)

        # art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

        # debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
        #                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
        debris_info = ImageInfo([320, 240], [640, 480])
        debris_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png")
        debris_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png")
        debris_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")
        debris_image4 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_brown.png")
        debris_image5 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png")
        debris_image6 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
        debris_image7 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_blue.png")
        debris_image8 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png")
        debris_image9 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png")

        # nebula images - nebula_brown.png, nebula_blue.png
        nebula_info = ImageInfo([400, 300], [800, 600])
        nebula_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")
        nebula_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")

        # splash image
        splash_info = ImageInfo([200, 150], [400, 300])
        splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

        # ship image
        ship_info = ImageInfo([45, 45], [90, 90], 35)
        ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

        # missile image - shot1.png, shot2.png, shot3.png
        # lifespan reduced from 50 ( = given value ) to 10
        missile_info = ImageInfo([5,5], [10, 10], 3, 10)
        missile_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")
        missile_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
        missile_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")

        # asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
        asteroid_info = ImageInfo([45, 45], [90, 90], 40)
        asteroid_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
        asteroid_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
        asteroid_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")

        # animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
        explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
        explosion_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
        explosion_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
        explosion_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
        explosion_image4 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

        # sound assets purchased from sounddogs.com, please do not redistribute
        soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
        missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
        missile_sound.set_volume(.5)
        ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
        explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
        self.init2()
        return

    def init2(self):
        global debris_info, nebula_info, splash_info,             \
               ship_info, missile_info, asteroid_info,            \
               explosion_info
        global debris_image1, debris_image2, debris_image3,       \
               debris_image4, debris_image5, debris_image6,       \
               debris_image7, debris_image8, debris_image8,       \
               debris_image9,                                     \
               nebula_image1, nebula_image2,                	  \
               splash_image, ship_image,                          \
               missile_image1, missile_image2, missile_image3,    \
               asteroid_image1, asteroid_image2, asteroid_image3, \
               explosion_image
        global soundtrack, missile_sound, ship_thrust_sound,      \
               explosion_sound
        global my_ship, a_rock, a_missile
        global rock_group, missile_group

        global myRandomSeed
        global started, score, lives

        # Stop Sound
        soundtrack.rewind()
        missile_sound.rewind()
        ship_thrust_sound.rewind()
        explosion_sound.rewind()
       
        started = False
        lives = NUMBER_OF_LIVES

        # initialize ship
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        
        # create a static Rock
        #a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.1, asteroid_image, asteroid_info)
        #self.generate_static_rock()
        rock_group = []
        self.rock_spawner()

        # create a static Missile 
        #a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image1, missile_info, missile_sound)
        missile_group = []
        #a_missile = self.generate_static_missile()

        return

    # 5 Define event handlers

    def group_collide(self, sprite_group, other_object, number_of_lives = 0):
        """Check for collisions of object with group"""
        for sprite in sprite_group:
            if sprite.collide(other_object):
                sprite_group.remove(sprite)
                number_of_lives -=1
        return number_of_lives
    
    def group_group_collide(self, group1, group2):
        """Check for collision of 2 groups"""
        number_of_collisions = 0
        sum_of_collisions = 0
        for group1_member in group1:
            number_of_collisions = -self.group_collide(group2, group1_member)
            sum_of_collisions += number_of_collisions
            if number_of_collisions > 0:
                group1.remove(group1_member)
        return sum_of_collisions
    
    def process_sprite_group(self, canvas, sprite_group):
        """Visualize the sprites on the screen"""
        for sprite in sprite_group:
            sprite.draw(canvas)
            if not sprite.update():
                sprite_group.remove(sprite)
        return
    
    # mouseclick handlers that reset UI and conditions whether splash image is drawn
    def click(self, pos):
        global started, score
        center = [WIDTH / 2, HEIGHT / 2]
        size = splash_info.get_size()
        inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        if (not started) and inwidth and inheight:
            started = True
            # Reset score just when new game starts
            score = 0

    def draw(self, canvas):
        """ Draw Handler """
        global time
        global debris_info, nebula_info, splash_info,             \
               ship_info, missile_info, asteroid_info,            \
               explosion_info
        global debris_image1, debris_image2, debris_image3,       \
               debris_image4, debris_image5, debris_image6,       \
               debris_image7, debris_image8, debris_image8,       \
               debris_image9,                                     \
               nebula_image1, nebula_image2,                	  \
               splash_image, ship_image,                          \
               missile_image1, missile_image2, missile_image3,    \
               asteroid_image1, asteroid_image2, asteroid_image3, \
               explosion_image
        global soundtrack, missile_sound, ship_thrust_sound,      \
               explosion_sound
        global my_ship, a_rock, a_missile
        global lives, score
        global started

        # animiate background
        time += 1
        center = debris_info.get_center()
        size = debris_info.get_size()
        wtime = (time / 8) % center[0]
        canvas.draw_image(nebula_image2, nebula_info.get_center(), nebula_info.get_size(), [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
        canvas.draw_image(debris_image5, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]],
                                [WIDTH/2+1.25*wtime, HEIGHT/2], [WIDTH-2.5*wtime, HEIGHT])
        canvas.draw_image(debris_image5, [size[0]-wtime, center[1]], [2*wtime, size[1]],
                                [1.25*wtime, HEIGHT/2], [2.5*wtime, HEIGHT])

        # check for collisions
        lives = self.group_collide(rock_group, my_ship, lives)
        score += self.group_group_collide(missile_group, rock_group)
            
        if (lives <= 0):
            started = False
            # it is important NOT to load the sounds again,
            # but just to stop it!
            self.init2()
        
        if started:
            # draw ship and update ship
            my_ship.draw(canvas)
            my_ship.update()

            # draw sprites and update sprites
            #a_rock.draw(canvas)
            #a_rock.update()
            self.process_sprite_group(canvas, rock_group)

            # draw missiles and update missiles
            #a_missile.draw(canvas)
            #a_missile.update()
            self.process_sprite_group(canvas, missile_group)
        
            # update score and lifes
            canvas.draw_text("Lives  "+ str(lives), (WIDTH/8, 50), 24, "White")
        else:
            # draw splash screen if not started
            canvas.draw_image(splash_image, splash_info.get_center(), 
                              splash_info.get_size(), [WIDTH/2, HEIGHT/2], 
                              splash_info.get_size())
        # Display score of current game
        # and display highscore of last game, while waiting for new game
        canvas.draw_text("Score  "+ str(score), (WIDTH-WIDTH/4, 50), 24, "White")
        return

    # timer handler that spawns a rock
    def rock_spawner(self):
        if started:      
            #global rock_group
            #global a_rock
            #a_rock = self.generate_dynamic_rock()
            #a_rock = self.generate_static_rock()
            # just generate a rock if there are less than 12
            # rocks in space
            if (len(rock_group) < 12):
                rock_group.append(self.generate_dynamic_rock())
            return
        
    # Generation of a rock with static parameters	
    def generate_static_rock(self):
        global asteroid_image1, asteroid_info
        rock_pos = [WIDTH / 3, HEIGHT / 3]
        rock_vel = [1, 1]
        rock_ang = 0
        rock_ang_vel = 0
        rock_image = asteroid_image1
        rock_info = asteroid_info
        return Sprite(rock_pos, rock_vel, rock_ang, rock_ang_vel, rock_image, rock_info)
    
    # Generation of a rock with dynamic parameters	
    def generate_dynamic_rock(self):
        global asteroid_image1, asteroid_image2, asteroid_image3, \
               asteroid_info
        global my_ship
        
        # rock position must be in some distance of ship
        # to make it easy, the distance is always positive, 
        # but of course by modulo arithmetics the rock is kept on screen
        #rock_pos = [random.randrange(0,WIDTH,1), random.randrange(0,HEIGHT,1)]
        rock_pos = [(my_ship.pos[0]+random.randrange(-WIDTH/4,WIDTH/4,1) + WIDTH/2) % WIDTH, 
                    (my_ship.pos[1]+random.randrange(-HEIGHT/4,HEIGHT/4,1) + HEIGHT/2) % HEIGHT]
        rock_vel = [random.randrange(self.ROCK_MINSPEED, self.ROCK_MAXSPEED,1), \
                    random.randrange(self.ROCK_MINSPEED, self.ROCK_MAXSPEED,1)]
        rock_ang = random.randrange(0, 360, 1)/(2*math.pi)
        rock_ang_vel = random.randrange(self.ROCK_MIN_ANGVEL, self.ROCK_MAX_ANGVEL, 1)*self.SHIP_ANGLE_VELOCITY
        # Random asteroid selection
        #rock_image = asteroid_image1
        # initialize asteroid dic
        asteroid_image_dic = { 0: asteroid_image1, 1:asteroid_image2, 2:asteroid_image3}
        rock_image = asteroid_image_dic[random.randrange(0, 3, 1)]
        rock_info = asteroid_info
        return Sprite(rock_pos, rock_vel, rock_ang, rock_ang_vel, rock_image, rock_info)
        
    # Generation of a missile with static parameters	
    def generate_static_missile(self):
        global missile_image1, missile_image2, missile_image3, \
               missile_info, missile_sound
        newmissile_pos = [2 * WIDTH / 3, 2 * HEIGHT / 3]
        newmissile_vel = [-1,1]
        newmissile_ang = 0
        newmissile_ang_vel = 0
        newmissile_image = missile_image2
        newmissile_info = missile_info
        newmissile_sound = missile_sound
        return Sprite( newmissile_pos, newmissile_vel, newmissile_ang, newmissile_ang_vel, \
                            newmissile_image, newmissile_info, newmissile_sound)        

    def keydown(self, key):
        if started:
            """ Key pressed """
            #print "keydown = ", key, int(key)
            if (key == 37): # key "arrow left"
                my_ship.angle_vel = -self.SHIP_ANGLE_VELOCITY
            if (key == 39): # key "arrow right"
                my_ship.angle_vel = self.SHIP_ANGLE_VELOCITY
            if (key == 38): # key "arrow up"
                my_ship.thrust = True
            if (key == 32): # key "space"
                my_ship.shoot()
        return 
   
    def keyup(self, key):
        """ Key released """
        if started:
            if (key == 37): # key "arrow left"
                my_ship.angle_vel = 0
            if (key == 39): # key "arrow right"
                my_ship.angle_vel = 0
            if (key == 38): # key "arrow up"
                my_ship.thrust = False
            if (key == 32): # key "space"
                # Also shoot if you rise the key = double frequency
                #my_ship.shoot()
                pass
        return 

    # This function is executed to start the application
    def main(self):
        """ Class start function """
        self.init()

        # 6 Initialize frame
        global frame
        frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

        # 7 register handlers
        frame.set_draw_handler(self.draw)
        timer = simplegui.create_timer(1000.0, self.rock_spawner)

        frame.set_keydown_handler(self.keydown)
        frame.set_keyup_handler(self.keyup)
    
        frame.set_mouseclick_handler(self.click)

        # 8 # get things rolling
        timer.start()
        frame.start()

        return

# always remember to check your completed program against the grading rubric

# 9 run your code
asteroids = AsteroidsGame()
asteroids.main()
