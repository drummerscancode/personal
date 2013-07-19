#!/usr/bin python
''' 
TODO: 
	Performance 
	Do it more pythonically with generators.
'''
from itertools import permutations as P
import sys 
import operator

file = open(sys.argv[1])
lines = file.read().splitlines()
num_of_tests = int(lines[0])

for i in range(num_of_tests):
	num_of_coordinates = int(lines[i*3 + 1])
	permA = P(lines[i*3 + 2].split(' ')) # remove the spaces from the line
	permB = P(lines[i*3 + 3].split(' '))
	permA = [map(int, x) for x in permA] # change to int
	permB = [map(int, x) for x in permB]

	res = sys.maxint # start from something high
	for j in permA:		
		for k in permB:
			prod = reduce(operator.add, map(operator.mul, j, k))
			res = min(res, prod)
	print 'Case #%s: %s' % (str(i+1), res)

