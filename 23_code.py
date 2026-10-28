
a="mgosfmg@#$#$5fgdsm#$435.gmhl"
char=0
dig=0
spchar=0
for i in a:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        dig+=1
    else:
        spchar+=1
print("number of alphabets:", char)
print("number of digits:", dig)
print("number of special characters:", spchar)