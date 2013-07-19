import urllib
from string import digits

#file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=30075')
#print file.read()

counter = 0 # of tries
nothingOld = "58765" # start from this nothing
messages = [] # keeps messages that vary from the typical "and the next nothing is..."
while counter < 395: 
    counter += 1;
    file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothingOld)
    string = file.read()
    
    if len(string) > 30 or string[0:3] != "and":
        messages.append(string + nothingOld)
        
    nothingNew = ""
    for letter in string:
        if digits.find(letter) != -1:
            nothingNew += letter
    
    if nothingNew == nothingOld: # this never happens
        break
    else:
        nothingOld = nothingNew
        
print nothingOld, counter # the point where we stopped
print messages # here is the solution