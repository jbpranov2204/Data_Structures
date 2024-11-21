x = int(input("Enter your Number:"))

sum = 0

while x>0:
    x = x//10
    sum = sum + 1
 
print("The Count of the Digits is:",sum)   