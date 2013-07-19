import urllib
from PIL import Image

#image = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
file = Image.open("oxygen.png", "r")
#file.write(image.read())

l = list(file.getdata())
print len(l)
print file.getcolors()
i = 0
for line in l:
    print line,
    i += 1
