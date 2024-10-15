def Avg(l):
    sum = 0 
    for x in l:
        sum = sum+x
        n = len(l)
        return sum / n
    
if __name__ == '__main__':
    l = [10.20,30]
    print(Avg(l))



#def Avg(n):
  #return sum(l)/len(l)   
