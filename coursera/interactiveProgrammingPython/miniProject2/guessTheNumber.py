'''
    Guess the number game.
    Does some user input validation as well (checks for number in the correct range).
	Does not recalculate the guess_count every time.	
	TODO: do the opposite: user gives the number and the computer finds it.

	Submitted as http://www.codeskulptor.org/#user11_mnUV0UB7U12xjJD.py

	
'''
import Tkinter # simplegui
import random
import math


text_box = '' # the text_box for the guesses, due to dynamic typing the var changes.
comp_number = 0 # the secret generated from the computer
guess_range = 0 # the upper limit of guesses, 0-100 or 0-1000
guesses_remaining = 0
cached_initial_guesses = {} # over-engineering: cache the guess count and don't recalculate them. 
DEFAULT_RANGE = 100 # this is the default according to description


def calculate_initial_guesses(guess_range):
	''' 
		Computes the number of guesses allowed as log2(range)
		and caches the result for reuse. 
    '''
	guess_count = math.ceil(math.log(guess_range, 2))
	cached_initial_guesses[guess_range] = guess_count
	return guess_count


def generate_secret(guess_range):
	''' Generates a new secret in the specified range. '''
	return random.randrange(guess_range)


def range100():
	''' Restarts game with range = 100. '''
	start_game(100)


def range1000():
	''' Restarts game with range = 1000. '''
	start_game(1000)	

    
def get_input(guess):
	'''
		Event handler for input field.
		Reduces remaining guesses and gives directions to player2.
	'''
	global guesses_remaining

	try:
		user_number = int(guess)
	except ValueError:
		print('Give a number please.\n') # sys.exit not available in sculptor.
		return

	# Optional: checks the input against the guess range
	if user_number < 0 or user_number >= guess_range:
		print('Please give a number between [0 - %d)\n' % guess_range) # raise ValueError('') here
		return
	
	guesses_remaining -= 1
	print('Guess was %d' % user_number)
	print('Number of remaining guesses is %d' % guesses_remaining)

	if guesses_remaining == 0 and user_number != comp_number:
		print('You lost! The number was %d\n' % comp_number)
		start_game(guess_range) # restart with the same guess range
	else: # guesses_remaining > 0:
		if user_number < comp_number:
			print('Higher!\n')
		elif user_number == comp_number:
			print('Correct!\n')
			start_game(guess_range) # restart
		else:
			print('Lower!\n')


def start_game(g_range):
	'''
		(int) -> None
		Starts a game by
		generating a new secret in the specified range 
		and resetting the guess count.
	'''
	global guess_range, comp_number, guesses_remaining
	guess_range = g_range
	comp_number = generate_secret(guess_range)
	guesses_remaining = cached_initial_guesses[guess_range] if guess_range in cached_initial_guesses else calculate_initial_guesses(guess_range)
	
	print('New game...Range is [0 - %d)' % guess_range)
	print('Number of remaining guesses is %d' % guesses_remaining)
	text_box.set_text('') # reset the input


def main():
	''' Creates the frame and starts the default game. '''
	global text_box
	# Create the gui
	frame = simplegui.create_frame('Guess the number', 200, 200) 
	text_box = frame.add_input("Enter your guess:", get_input, 100)
	button = frame.add_button('Range 0-100', range100, 100)
	button = frame.add_button('Range 0-1000', range1000, 100)
	# Start a game in the default 0-100 range.
	start_game(DEFAULT_RANGE)

	frame.start() # works even without it


if __name__ == '__main__':
	main()
