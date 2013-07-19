#!/usr/bin python
import sys
import re

file = open(sys.argv[1])
lines = file.read().splitlines() # nice way to remove the eol

parameters = lines[0].split(' ')	
L = int(parameters[0])
D = int(parameters[1])
N = int(parameters[2])

words = lines[1: 1 + D]
patterns = lines[1+D: 1+D+N]

index = 1 # index of case
for pattern in patterns:
	counter = 0 # counter of how many times the word appears
	pattern = pattern.replace('(', '[')
	pattern = pattern.replace(')',']')
	expression = re.compile(pattern)

	for word in words:
		res = expression.findall(word)
		counter += len(res)

	print 'Case #' + str(index) + ': ' + str(counter)		
	index += 1 
