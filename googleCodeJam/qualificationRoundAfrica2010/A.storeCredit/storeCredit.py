#! /usr/bin python
import itertools
file = open('A-large-practice.in.in')

lines = file.readlines()
numOfTests = int(lines[0])

for i in range(0, numOfTests):
	credit = int(lines[i*3 +1])
	items = lines[i*3 +3].split(' ')
	com = itertools.combinations(items, 2) #keeps order

	for c in com:
		if (int(c[0]) + int(c[1])) == credit:
			ind1 = items.index(c[0]) + 1
			if (c[0]==c[1]): 
				items.remove(c[0])
				ind2 = items.index(c[1]) + 2 
			else: ind2 = items.index(c[1]) +1 
			items.remove(c[1])
			print 'Case #' + str(i+1) + ': ' + str(ind1) + ' ' + str(ind2)
			break

