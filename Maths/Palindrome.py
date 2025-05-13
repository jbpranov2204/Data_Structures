def isPal(n):

    rev = 0
    temp = n

    while temp != 0:
        ld = temp % 10 #extracts last digit from the number
        rev = rev*10 + ld
        temp = temp // 10

    return rev == n
    
if __name__=='__main__':
    num = int(input("Enter the Number:"))
    print(isPal(num))

