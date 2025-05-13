def getEvenOdd(l):
    even = []
    odd = []

    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
          odd.append(i)

    return even,odd          


l = [12,28,17,83,36,22]
even,odd = getEvenOdd(l)
print(even)
print(odd)

