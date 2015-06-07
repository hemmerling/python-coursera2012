#!/usr/bin/env python
import simplegui

# Handler to draw on canvas
def draw(canvas):
    # Draw two circles with radius 20 and white lines of width 10. 
    # One is centered at (90,200) and one at (210,200).
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210, 200], 20, 10, "White")
    # Draw a red line of width 40 from (50,180) to (250,180).
    canvas.draw_line((50, 180), (250, 180), 40, "Red")
    # Draw two red lines of width 5 from (55,170) to (90,120) and from (90,120) to (130,120).
    canvas.draw_line((55, 170), (90, 120), 5, "Red")
    # Draw a red line of width 140 from (180,108) to (180,160).
    canvas.draw_line((180, 108), (180, 160), 140, "Red")
    
# Create a frame and assign callbacks to event handlers
# Create a 300-by-300 canvas.
frame = simplegui.create_frame("Home", 300, 300)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
