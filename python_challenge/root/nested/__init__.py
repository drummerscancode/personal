import pickle
import urllib

file = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
a = pickle.load(file)

for line in a:
    for i in range(len(line)):
        print line[i],
    print "EOL"
    
