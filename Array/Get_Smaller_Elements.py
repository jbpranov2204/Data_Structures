def getSmaller(l,x):
    res = []

    for e in l:
        if e < x:
            res.append(e)
    return res

l = [32,10,18,33]
x = 20
print(getSmaller(l,x))


