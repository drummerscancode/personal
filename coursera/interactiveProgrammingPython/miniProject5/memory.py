# Memory game
# Extras: 
#	unpaired cards are colored red and covered up after 0.5 secs 
#		(instead of waiting for the next click).
#	after finishing the game a message is displayed
#		and the game restarts after 1 sec.
# Submitted as http://www.codeskulptor.org/#user14_yZx2bxEECr6Bd9Q.py

import simplegui
import random
deck = [] # the deck of cards
exposed = [] # flag indicating whether the card is exposed or not
state = 0 # the number of clicked cards
counter_attempts = 0 
card1_index = -1 # the first card clicked in the round
card2_index = -1 # the second card clicked in the round
CARD_WIDTH = 50
CARD_HEIGHT = 100
   
    
def init():
    """ Initializes a new game by resetting the counters etc. """
    global deck, exposed, state, counter_attempts, card1_index, card2_index
    global cover_timer, restart_timer
    
    deck = range(8) * 2
    random.shuffle(deck) # shuffle the cards
    exposed = [False for card in deck]
    state = 0
    counter_attempts = 0
    card1_index, card2_index = -1, -1
    if restart_timer.is_running():
        restart_timer.stop()
    

def check_cards():
    """ 
    Checks if the last 2 cards clicked
    depict the same card. 
    """
    if deck[card1_index] == deck[card2_index]:
        return True
    return False


def cover_cards():
    """ 
    Cover back both cards if the second clicked 
    is not the same as the first one.
    """
    global state, timer, card1_index, card2_index
    if cover_timer.is_running():
        exposed[card1_index] = False
        exposed[card2_index] = False
        card1_index, card2_index = -1, -1
        state = 0
        cover_timer.stop()
    
    
def mouseclick(pos):
    global timer, exposed, state, counter_attempts, card1_index, card2_index

    card_clicked = pos[0] // CARD_WIDTH # index of the card clicked
    if not exposed[card_clicked] and state < 2: # if it is already exposed don't do anything
        exposed[card_clicked] = True # show it for now
        state += 1
        
        if state == 1:
            card1_index = card_clicked
        else: # state == 2
            card2_index = card_clicked
            counter_attempts += 1
            if not check_cards(): # they are not the same
                cover_timer.start() # cover them up
            else: # the cards match
                state = 0
        
                           
def draw(canvas):
    """ Takes care of the canvas. """ 
    index = -1
    for card in deck:
        index += 1 
        if exposed[index]: # display the card
            if (index == card1_index or index == card2_index) and state == 2 and not check_cards(): # 
                color = "Red" # use red color if the cards do not match
            else: 
                color = "White"
            canvas.draw_text(str(card), (index * CARD_WIDTH + CARD_WIDTH/2, CARD_HEIGHT/2 + 10), 20, color)
            
        else: # display the cover
            canvas.draw_polygon([(index*CARD_WIDTH, 0), ((index+1)*CARD_WIDTH, 0), ((index+1)*CARD_WIDTH, CARD_HEIGHT), (index*CARD_WIDTH, CARD_HEIGHT) ], 2, "Green")

    counter_label.set_text('Moves = ' + str(counter_attempts))
    
    if all(exposed):
        canvas.draw_text('Congrats, you finished in ' + str(counter_attempts) + ' moves', (200, CARD_HEIGHT/2 + 5), 25, 'Yellow')
        restart_timer.start()


# Create GUI
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
counter_label = frame.add_label("Moves = 0")
cover_timer = simplegui.create_timer(500, cover_cards) # timer to cover up cards 
restart_timer = simplegui.create_timer(1000, init) # timer to restart the game
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

init()
frame.start()
