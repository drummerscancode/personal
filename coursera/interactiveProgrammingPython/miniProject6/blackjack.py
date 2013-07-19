# http://www.codeskulptor.org/#user15_fpL667ewCEq2ru5.py
# Mini-project #6 - Blackjack
# Extras: 	display the deck somewhere
# 			separate prompt and outcome messages
import simplegui
import random

# card graphics
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

in_play = False # are we in a game?
outcome = '' # the outcome of the game to be displayed
prompt = '' # prompt the user for action
score = 0 # the player's score 
deck = None # the deck of remaining cards
player_hand = None 
dealer_hand = None
DEAL_MSG = 'Press deal when ready!'


class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, hidden):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        
        if hidden:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0 # keep the value in order not to call update_value all the time

    def __str__(self):
        return ', '.join([str(card) for card in self.hand]) + ': ' + str(self.value)

    def add_card(self, card):
        ''' Adds a card to the hand and updates its value. '''
        self.hand.append(card)
        self.value = self._update_value()
        
        
    def _update_value(self):
        # Marked as private method
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        aces_counter = 0 # counter of how many aces exist in the hand,
                         # not needed for blackjack even if you have 2 aces 
                         # only one can count as 11, but what if we play 31? ;)
        for card in self.hand:
            if card.rank == 'A':
                aces_counter += 1
            value += VALUES[card.rank]
            
        for i in range(aces_counter):
            if value <= 11: # if we won't bust..
                value += 10 # add 10 (also a simplification of the game)
                
        return value

   
    def draw(self, canvas, pos):
        index = 0
        for card in self.hand:
            card.draw(canvas, [pos[0] + index*15, pos[1]], False)
            index += 1
       
            
    def draw_dealer_hand(self, canvas, pos):
        """ Hides the first card. """
        index = 0
        for card in self.hand:
            card.draw(canvas, [pos[0] + index*15, pos[1]], not bool(index) )
            index += 1    
    
    def is_busted(self):
        return True if self.value > 21 else False
        
        
class Deck:
    def __init__(self):
        self.deck = []

    def shuffle(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.deck) 

    def deal_card(self):
        global prompt
        
        try:
            return self.deck.pop() # deal the *last* card object from the deck
        except: # IndexError not defined in CodeSkulptor
            # this would bot happen as the current deal creates a new deck
            prompt = 'Desk is empty, please deal.'
            
    def __str__(self):
        return ', '.join([str(card) for card in self.deck])

    def draw(self, canvas, pos):
        """ Display only 10 cards for aesthetic reasons. """
        index = 0
        for card in self.deck:
            if index == 10: 
                break
            card.draw(canvas, [pos[0] + index*2, pos[1]], True)
            index += 1

            
def deal():
    """ Start a new game, shuffle cards and deal_hands. """
    global outcome, score, deck, player_hand, dealer_hand, in_play, prompt
    
    outcome = ''
    if in_play: # we were in the middle of a game
        outcome = 'Player lost previous game!' 
        score -= 1
        
    deck = Deck() # create a new deck
    deck.shuffle() # and shuffle it 
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    
    prompt = 'Hit or stand?'    
    in_play = True

    
def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global player_hand, outcome, score, in_play, prompt
    
    if in_play:
        if not player_hand.is_busted(): # is this necessary? since we are in a game
            player_hand.add_card(deck.deal_card())
            
            if player_hand.is_busted():
                outcome = 'Player busted!'
                prompt = ''
                in_play = False
                score -= 1 # max(score-1, 0) don't allow to drop below 0 
            else: outcome = ''
    else:
        prompt = DEAL_MSG
        outcome = ''   
       
        
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global outcome, in_play, score, dealer_hand, prompt
    
    if in_play:
        while dealer_hand.value < 17: # here a simplification of the game
            dealer_hand.add_card(deck.deal_card())
            
        if dealer_hand.is_busted():
            outcome = 'Dealer busted!'
            score += 1
        elif dealer_hand.value < player_hand.value:
            outcome = 'Player wins!'
            score += 1
        else: 
            outcome = 'Dealer wins!'
            score -= 1
        in_play = False 
        prompt = ''
        
    else: # we are not in a game      
        prompt = DEAL_MSG
        outcome = ''

 
def draw(canvas):
    canvas.draw_text('Blackjack', [CANVAS_WIDTH-100, 20], 20, 'Red')
    canvas.draw_text('Score: ' + str(score), [10, 0.2*CANVAS_HEIGHT], 15, 'White')
    canvas.draw_text('Player\'s hand: ', (10, 0.25*CANVAS_HEIGHT), 15, 'White')
    canvas.draw_text('Dealer\'s hand: ', (10, 0.7*CANVAS_HEIGHT), 15, 'White')
    canvas.draw_text(outcome, [CANVAS_WIDTH/2, CANVAS_HEIGHT - 10], 20, 'Yellow')
    canvas.draw_text(prompt, [CANVAS_WIDTH-150, 0.5*CANVAS_HEIGHT - 10], 15, 'Yellow')

    if player_hand:
        player_hand.draw(canvas, (CANVAS_WIDTH/2, 0.25*CANVAS_HEIGHT)) 
    if dealer_hand:
        if in_play: # hide the first card
            dealer_hand.draw_dealer_hand(canvas, (CANVAS_WIDTH/2, 0.7*CANVAS_HEIGHT)) 
        else:
            dealer_hand.draw(canvas, (CANVAS_WIDTH/2, 0.7*CANVAS_HEIGHT))    
    if deck:
        deck.draw(canvas, (CANVAS_WIDTH - 150, 0.5*CANVAS_HEIGHT)) 

    

frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
frame.add_button("Deal", deal, 100)
frame.add_button("Hit",  hit, 100)
frame.add_button("Stand", stand, 100)
frame.set_draw_handler(draw)

prompt = DEAL_MSG
frame.start()
