def largest(l):
    for i in l:
        for j in l:
            if j > i:
                break
        else:
            return i
        
def secondLargest(l):
    lar = largest(l)
    slar = None
    for x in l:
        if x != lar:
            if slar == None:
                slar = x
            else:
                if x > slar:
                    slar = x
                elif slar > x:
                    slar = slar
    return slar
    

arr = [123,4234,5434,523,42,234]
print(secondLargest(arr))
        
