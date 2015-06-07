#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   coursera2012
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @version   1.00
#  @date      2015-01-01
#  @copyright Apache License, Version 2.0
#
#  mock objects for simplegui
#  the mocks do nothing but allow the code to run
#  to actually unit test your code, call the event
#  handlers in your code directly
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

# store the string written to screens so can check it from test
current_drawn_strings = []
timer_running = False

KEY_MAP = { "down" : 40,  "up": 38, "S" : 83, "W" : 87, "H" : 72}

class Label:
  def set_text(l, text):
    return Label()

class Frame:
  def add_button(f, label, handler, width=100):
    pass
  def add_input(f, label, handler, width):
    pass
  def start(f):
    pass
  def set_draw_handler(f, function):
    pass
  def set_keydown_handler(f, key):
    pass
  def set_keyup_handler(f, key):
    pass
  def add_label(f, label):
    return Label()
  def set_mouseclick_handler(f, handler):
    pass
  def set_canvas_background(f, color):
    pass

class Timer:
  def start(t):
    global timer_running
    timer_running = True
  def stop(t):
    global timer_running
    timer_running = False
    pass

class Canvas:
  def draw_text(c, str, coords, font, color):
    global current_drawn_string
    current_drawn_strings.append(str)
    pass
  def draw_polygon(c, point_list, line_width, line_color, fill_color):
    pass
  def draw_image(c, image, center_source, width_height_source, center_dest, width_height_dest):
    pass
  def draw_circle(c, center_point, radius, line_width, line_color, fill_color=None):
    pass

class Sound:
  def play(c):
    pass

  def rewind(c):
    pass

  def set_volume(c, volume):
    pass

def create_frame(title, canvas_width, canvas_height, control_width=200):
  return Frame()

def create_timer(time, function):
  return Timer()

def load_image(url):
  pass

def load_sound(URL):
  return Sound()

