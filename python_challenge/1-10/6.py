import urllib
import os.path
import string
import zipfile

## find channel.zip
obj = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
file = open("6", "wb")
file.write(obj.read())
zip = zipfile.ZipFile("channel.zip", "r")

## to open the path
#currentDir = dirname(abspath("."))
#channelDir = join(currentDir, 'channel')
#filepath = join(channelDir, fileID + '.txt')

## 
fileID = "90052" # the text file to read
fileIDs = []
while True:    
    fileIDs.append(fileID)
    file = open("./channel/" + fileID + ".txt", "rb")
    message = file.read()
    words = message.rsplit()
    #filter(lambda x: string.digits.find(x), words[len(words) - 1]))
    if string.digits.find(words[len(words)-1][0]) != -1: # checks the first letter of the last word in the message
        fileID = words[len(words)-1]
    else:
        break

print message, fileID # collect the comments

## collect the comments from the contents of the zip
print ''.join(zip.getinfo(i+".txt").comment for i in fileIDs)