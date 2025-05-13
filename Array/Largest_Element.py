def largest(l):
    for i in l:
        for j in l:
            if j > i:
                break
        else:
            return i