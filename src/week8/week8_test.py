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
from asteroids import ImageInfo
from asteroids import Ship
from asteroids import Sprite
from asteroids import AsteroidsGame

#from asteroids import ship_image

ship_image = None

class ImageInfo_getCenterTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        center = [1,1]
        size = 1
        self.imageinfo = ImageInfo(center, size)

    def testGetCenter(self):
        center = [1,1]
        self.imageinfo.center = center
        assert self.imageinfo.get_center() == center, 'ImageInfo.get_center() does not provide the right return value'

class ImageInfo_getSizeTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        center = [1,1]
        size = 1
        self.imageinfo = ImageInfo(center, size)

    def testGetSize(self):
        size = 1
        self.imageinfo.size = size
        assert self.imageinfo.get_size() == size, 'ImageInfo.get_size() does not provide the right return value'

class ImageInfo_getRadiusTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        center = [1,1]
        size = 1
        self.imageinfo = ImageInfo(center, size)

    def testGetRadius(self):
        radius = 1
        self.imageinfo.radius = radius
        assert self.imageinfo.get_radius() == radius, 'ImageInfo.get_radius() does not provide the right return value'

class ImageInfo_getLifespanTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        center = [1,1]
        size = 1
        self.imageinfo = ImageInfo(center, size)

    def testGetLifespan(self):
        lifespan = 1
        self.imageinfo.lifespan = lifespan
        assert self.imageinfo.get_lifespan() == lifespan, 'ImageInfo.get_radius() does not provide the right return value'

class ImageInfo_getAnimatedTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        center = [1,1]
        size = 1
        self.imageinfo = ImageInfo(center, size)

    def testGetAnimated(self):
        animated = False
        self.imageinfo.lifespan = animated
        assert self.imageinfo.get_animated() == animated, 'ImageInfo.get_animated() does not provide the right return value'

class Ship_drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        global ship_image
        self.asteroids = AsteroidsGame()
        self.asteroids.init()
        pos = [1,1]
        vel = [1,1]
        angle = 0
        image = ship_image

        center = [1,1]
        size = 1
        info = ImageInfo(center, size)

        self.ship = Ship( pos, vel, angle, image, info)

    def testDraw(self):
        canvas = Canvas()
        self.ship.pos = [1,1]
        self.ship.radius = 0
        assert self.ship.draw(canvas) == None, 'Ship.draw() does not provide the right return value'

class Ship_updateTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        global ship_image
        self.asteroids = AsteroidsGame()
        self.asteroids.init()
        pos = [1,1]
        vel = [1,1]
        angle = 0
        image = ship_image

        center = [1,1]
        size = 1
        info = ImageInfo(center, size)

        self.ship = Ship( pos, vel, angle, image, info)

    def testUpdate(self):
        assert self.ship.update() == None, 'Ship.draw() does not provide the right return value'

class Sprite_drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        pos =[0,0]
        vel = [0,0]
        ang = 0.0
        ang_vel= [0,0]
        image = None

        center = [1,1]
        size = 1
        info = ImageInfo(center, size)

        self.sprite = Sprite(pos, vel, ang, ang_vel, image, info)


    def testDraw(self):
        canvas = Canvas()
        assert self.sprite.draw(canvas) == None, 'Sprite.draw() does not provide the right return value'

class Sprite_updateTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        pos =[0,0]
        vel = [0,0]
        ang = 0.0
        ang_vel= [0,0]
        image = None

        center = [1,1]
        size = 1
        info = ImageInfo(center, size)

        self.sprite = Sprite(pos, vel, ang, ang_vel, image, info)

    def testUpdate(self):
        assert self.sprite.update() == None, 'Sprite.update() does not provide the right return value'

class AsteroidsGame_initTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.asteroids = AsteroidsGame()

    def testInit(self):
        assert self.asteroids.init() == None, 'AsteroidsGame.init() does not provide the right return value'

class AsteroidsGame_angleToVectorTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.asteroids = AsteroidsGame()

    def testAngle_ToVector(self):
        vector = [1, 0]
        assert self.spaceship.angle_to_vector(0) == vector, 'AsteroidsGame.angle_to_vector() does not provide the right return value'

class AsteroidsGame_distTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.asteroids = AsteroidsGame()

    def testDist(self):
        a = [0, 1]
        b = [0, 0]
        dist = 1
        assert self.asteroids.dist(a,b) == dist, 'AsteroidsGame.init() does not provide the right return value'

class AsteroidsGame_drawTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.asteroids = AsteroidsGame()
        self.asteroids.init()

    def testDraw(self):
        canvas = Canvas()
        assert self.asteroids.draw(canvas) == None, 'AsteroidsGame.draw() does not provide the right return value'

class AsteroidsGame_rockSpawnerTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.asteroids = AsteroidsGame()

    def testRockSpawner(self):
        assert self.asteroids.rock_spawner() == None, 'AsteroidsGame.rock_spawner() does not provide the right return value'

class AsteroidsGame_mainTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.asteroids = AsteroidsGame()

    def testMain(self):
        assert self.asteroids.main() == None, 'AsteroidsGame.main() does not provide the right return value'

# run all tests
if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

