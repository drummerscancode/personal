# string.maketransbb(intab, outtab)

encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = " .,'"

for letter in url: # encrypted
    if punctuation.find(letter) != -1:
        print letter,
    else:
        print alphabet[(alphabet.find(letter) + 2)%26],