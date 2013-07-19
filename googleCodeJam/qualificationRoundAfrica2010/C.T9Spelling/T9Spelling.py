#! /usr/bin python
import sys

### Preface
file = open(sys.argv[1])
lines = file.readlines()
num_of_tests = int(lines[0])

### Dictionary
translate = {'a':'2', 'b':'22', 'c':'222', 'd':'3', 'e':'33', 'f':'333', 'g':'4', 'h':'44', 'i':'444', 'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66','o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99', 'y':'999', 'z':'9999', ' ': '0'}


for i in range(1, num_of_tests + 1):
	line = lines[i]
	translation = []
	translation.append(translate[line[0]])
	
	for j in range(1, len(line) - 1): # -1 for the \n character
		if translate[line[j-1]] in translate[line[j]] or translate[line[j]] in translate[line[j-1]]: # if they have a number in common means they are in the same key set
			translation.append(' ')

		translation.append(translate[line[j]])

	print 'Case #' + str(i) + ': ' + ''.join(translation)
