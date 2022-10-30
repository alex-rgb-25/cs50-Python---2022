import sys
names =[]
while True:
    try:
        txt = input("Name: ")
        names.append(txt)
    except EOFError:
        break
res = "Adieu, adieu, to "
if len(names) > 2:
    newNames = names[0:-1]
    for name in newNames:
        res += name+", "
    #res = res[0:-2]
    res += "and " + names[len(names)-1]
    print(res)
elif len(names) == 2:
    res += names[0] + " and " + names[1]
    print(res)
else:
    print(res + names[0])
