# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#
# Submitted: http://www.codeskulptor.org/#user10_SNBdBIWpbM_0.py

import random
import sys

def number_to_name(number):
	''' (number) -> string 
	
	Maps number selections to names.
	'''
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'Spock'
	elif number == 2:
		return 'paper'
	elif number == 3:
		return 'lizard'
	elif number == 4:
		return 'scissors'
	else:
		print('Please provide a number between 0 and 4 inclusive.')
		return None

    
def name_to_number(name):
	''' (string) -> number

	Maps name selection to corresponding number.
	Tests are insensitive to case (although not required).
	'''
	if name.lower() == 'rock':
		return 0
	elif name.lower() == 'spock':
		return 1
	elif name.lower() == 'paper':
		return 2
	elif name.lower() == 'lizard':
		return 3
	elif name.lower() == 'scissors':
		return 4
	else: 
		print('''You provided: %s.
Please provide instead one of rock, Spock, paper, lizard or scissors.''' % name)
		sys.exit() # exits the rest of the cases as well


def rpsls(name): 
	try:
		player_number = name_to_number(name)
	except SystemExit as e:
		print()
		return

	comp_number = random.randrange(5)
	difference = (player_number - comp_number)%5

	print('Player chooses %s' % name)
	print('Computer chooses %s' % (number_to_name(comp_number)))
	if difference == 0:
		print('Player and computer tie!')
	elif difference == 1 or difference == 2: # having difference <= 2 will not enter for 0 anyways because of the order of elifs, but it's implicit
		print('Player wins!')
	else: # the rest of the cases 3, 4
		print('Computer wins!')
	
	print() # an empty line
		

if __name__ == '__main__':
	rpsls("rock")
	rpsls("Spock")
	rpsls("paper")
	rpsls("lizard")
	rpsls("scissors")
