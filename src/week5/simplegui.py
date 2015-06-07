#!/usr/bin/env python
# mock objects for simplegui
# the mocks do nothing but allow the code to run
# to actually unit test your code, call the event handlers in your code directly

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

def create_frame(title, canvas_width, canvas_height, control_width=200):
  return Frame()

def create_timer(time, function):
  return Timer()
