#!/usr/bin python
'''
Greedy search
'''
import sys
import re

# text = 'So you\'ve registered. We sent you a welcoming email, to welcome you to code jam. But it\'s possible that you still don\'t feel welcomed to code jam. That\'s why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you\'ll feel very welcome. Very welcome, that is, to code jam.'
file = open(sys.argv[1])
lines = file.readlines()
num_of_tests = int(lines[0])

text = ''
original = 'welcome to code jam'
count = 0



def nice_formatting(cnt):
	''' cnt should be of type string '''
	while len(cnt) < 4:
		cnt = '0' + cnt
	cnt = cnt[len(cnt) - 4:]
	return cnt


def recursive_find(i, previous_index):
	global count
	if i == len(original):
		count += 1
#		print 'found!'
		return count

	indices = [m.start() for m in re.finditer(original[i], text[previous_index:])]
	for index in indices:
		recursive_find(i+1, previous_index + index)

	
def main():
	global text, count 
	for i in range(1, num_of_tests + 1):
		count = 0
		text = lines[i]
		indices = [m.start() for m in re.finditer(original[0], text)]
		for index in indices:
			recursive_find(1, index)
			
		print 'Case #' + str(i) + ': ' + nice_formatting(str(count))



if __name__ == "__main__":
	main()
