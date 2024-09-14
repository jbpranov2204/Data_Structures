def absolute(I):
        
        if I < 0:
            return -I
            
        return I
        
        
if __name__ == '__main__':
    num = int(input("Enter:"))
    print(absolute(num))