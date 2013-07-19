import pickle

unpickled = pickle.load(open("banner.p", "rb" ))
result = ""
for e in unpickled:
    for f in e:
        char = f[0]
        times = f[1]
        result += char*times
    result += "\n"
 
print result

# check: http://unixwars.com/2007/09/11/python-challenge-level-5-peak-hell/