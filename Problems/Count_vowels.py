str = "srth23457 45 ear"

vowels = 0
constants = 0
digits = 0
spl = 0


for i in range(0,len(str)):
    
    ch = str[i]
    
    if (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
        ch = ch.lower()
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            vowels = vowels+1
        else:
            constants = constants+1
    elif ('0' <= ch <= '9'):
        digits+=1
    else:
        spl+=1
        
print(vowels)
print(constants)
print(digits)
print(spl)