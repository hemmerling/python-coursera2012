# Write a Python program that initializes a global variable to 5. 
# The keydown event handler updates this global variable by doubling it, 
# while the keyup event handler updates it by decrementing it by 3.
#
# What is the value of the global variable after 12 separate key presses, 
# i.e., pressing and releasing one key at a time, and repeating this 12 times?
# To test your code, the global variable's value should be 35 after 4 key presses.

import simplegui

# initialize state
counter = 5

# event handlers
def keydown(key):
    global counter
    counter += counter
    print counter
    return

def keyup(key):
    global counter
    counter -= 3
    print counter
    return    
    
# create frame
frame = simplegui.create_frame("Echo", 35, 35)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
