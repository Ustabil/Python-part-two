# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []

DIFFICULTY = 8

# helper function to initialize globals
def new_game():
    global cards, exposed, DIFFICULTY
    for i in range(DIFFICULTY * 2):
        exposed.append(False)
    numbers = range(DIFFICULTY)
    cards = numbers
    cards.extend(numbers)
    random.shuffle(cards)
    print cards
    print exposed


# define event handlers
def mouseclick(pos):
    global exposed
    clicked = pos[0] / 50
    if exposed[clicked] == False:
        exposed[clicked] = True
        print "clicked card indexed: ", clicked



# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(len(cards)):
        canvas.draw_text(str(cards[i]), (i*50+15, 65), 48, 'White')
        if exposed[i] == False:
            canvas.draw_polygon([[i*50, 0], [i*50+50, 0], [i*50+50, 100], [i*50, 100]], 2, 'Black', 'Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
