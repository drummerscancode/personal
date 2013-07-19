#! /usr/bin python
'''
Problematic cases: wasdwasde
wewelcome should produce 3.
'''
import sys
import re
 
original = 'welcome to code jam'
# texts = ['elcomw elcome to', 'wweellccoommee to', 'welcometo']
text = "So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem \"welcome to code jam.\" After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."  # w?=e matches w if succeeded by e

file = open(sys.argv[1])
lines = file.readlines()
num_of_tests = lines[0]

expression = re.compile(r"(w+).*?(e+).*?(l+).*?(c+).*?(o+).*?(m+).*?(e+).*?(\s+).*?(t+).*?(o+).*?(\s+).*?(c+).*?(o+).*?(d+).*?(e+).*?(\s+)(j+).*?(a+).*?(m+).*?") # ? for greedyless
#res = expression.search(text)
#print res.group(1)

for i in range(1, int(num_of_tests) + 1): # texts:
	product = 0
	res = expression.search(lines[i])
	if res:
		product = res.group(1).count('w')
		for i in range(2, len(original) + 1): # 0 is the whole match
			product *= res.group(i).count(original[i - 1])
			
	print product
