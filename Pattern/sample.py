def maximum(n):
    for i in n:
        for j in n:
            if j>i:
                break
        else:
            return i


def pattern(n):
    a = maximum(n)
    for i in range(a,0,-1):
        for j in n:
            if i <= j:
                print('*', end='\t')
            else:
                print('', end='\t')
        print()
                
n = [4,3,2,1]
print(pattern(n))