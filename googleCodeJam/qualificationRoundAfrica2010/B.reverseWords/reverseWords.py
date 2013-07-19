#! /usr/bin/python

file = open('B-large-practice.in.in')
lines = file.readlines()

num_tests = lines[0]
#num_tests = raw_input('Enter number of tests:')
for i in range(1, int(num_tests)+1):
	#test = raw_input('Enter the test:')
	#words = test.split(' ')
	words = lines[i].strip('\n').split(' ')
	words.reverse()
	print 'Case #' + str(i) + ': ' + ' '.join(words)

