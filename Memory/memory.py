
# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []
state = 0
DIFFICULTY = 8
card1 = 0
card2 = 0
tries = 0


# helper function to initialize globals
def new_game():
    global cards, exposed, DIFFICULTY, state, tries

    #initialize the deck
    if len(exposed) > 0:
        temposed = []
        for i in exposed:
            temposed.append(False)
        exposed = temposed
    else:
        for i in range(DIFFICULTY * 2):
            exposed.append(False)
    numbers = range(DIFFICULTY)
    cards = numbers
    cards.extend(numbers)
    random.shuffle(cards)

    tries = 0
    state = 0

    #Uncomment for cheat mode!
    #print cards




# define event handlers
def mouseclick(pos):
    global exposed, state, card1, card2, tries
    clicked = pos[0] / 50
    if exposed[clicked] == True:
        return
    if state == 0:
        exposed[clicked] = True
        card1 = clicked
        state = 1
        return
    elif state == 1:
        exposed[clicked] = True
        card2 = clicked
        state = 2
        tries += 1
        return
    elif state == 2:
        if cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
        exposed[clicked] = True
        card1 = clicked
        state = 1
        return





# cards are logically 50x100 pixels in size
def draw(canvas):
    try_text = "Turns = " + str(tries)
    label.set_text(try_text)
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
