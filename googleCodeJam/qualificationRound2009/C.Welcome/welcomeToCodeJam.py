#! /usr/bin python
import sys
import re

file = open(sys.argv[1])
lines = file.readlines()
num_of_tests = lines[0]
string = 'welcome to code jam'
indices = []

for i in range(1, int(num_of_tests) + 1):
#	for j in range(len(string)):
#		indices = lines[i].find(string[j])
	re.findall(r"\w+|\sw\w+\selcome to code jam", lines[i]) 	
