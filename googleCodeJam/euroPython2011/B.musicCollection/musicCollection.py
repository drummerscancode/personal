#!/usr/bin python
'''
TODO: problem when reading more than 1 set
	problem with case 3 and 4
'''
from itertools import combinations as C
import sys
import re
sys.path.append("../..")
import tools

def find_unique_substrings(song, length):
	'''
	Finds substrings of the given length in the song
	that are unique among the songList.
	Returns a list of substrings (all of length size).
	'''
	combinations = []
	# combinations = C(song, length)
	for character in range(len(song) - length + 1):
		combinations.append(song[character: character + length])
	
	unique_substrings = []
	for combination in combinations:
		comb = ''.join(combination)
		if comb in song:
			occurInSong = song.count(comb) # number of times it occurs in the song
			if songList.count(comb) == occurInSong: # number of times it occurs in the songList is higher, therefore it's included in another song too
				# print comb + ' is NOT included elsewhere'
				unique_substrings.append(comb)
			
	return unique_substrings


file = open(sys.argv[1])
lines = file.readlines()
num_of_tests = int(lines[0])
total_num_songs = 0
songList = ''

for i in range(1, num_of_tests + 1):
	num_of_songs = int(lines[total_num_songs + i])
	songs = []
	for j in range(num_of_songs):
		songs.append(lines[total_num_songs + i + j + 1].upper().replace('\n', '')) # + 1 for the num_of_tests line
	songList = '\n'.join(songs)
	tools.print_case(i)

	for song in songs:
		ans = ''
#		if song == song[0]*len(song):
#			print 'change me' # song = song[0]
#			continue

		for k in range(1, len(song) + 1): # all lengths of substrings
			substrings = find_unique_substrings(song, k) 
			
			if len(substrings) > 0: # there was something returned
				ans = sorted(substrings)[0] 
				break # no reason to search the other lengths, since they are going to have more characters

		if ans == '':
			print ':('
#		elif ans == ' ':
#			print '""'
		else:	
			print '"' + ans + '"'

	total_num_songs += num_of_songs

