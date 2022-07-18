def pattern1():
    print("******PATTERN_1******")
    for i in range(1,4):
        for j in range(1,i+1):
            print(j, end=" ")
        print("")
pattern1()
print("")
def pattern2():
    print("******PATTERN_2******")         #inverted half pyramid patten 
    for i in range(3,0,-1):                  
        for j in range(1,i+1):
            print(j, end=" ")
        print("")
pattern2()
print("")

def pattern3():
    print("******PATTERN_3******")
    for i in range(1,4):
        for j in range(4-i-1):
            print(" ",end=" ")    
        for j in range(1,i+1):
            print(j, end=" ")
        print("")
pattern3()
print("")

def pattern4():
    print("******PATTERN_4******")         #inverted half pyramid patten 
    for i in range(3,0,-1):
        for j in range(4-i-1):
            print(" ",end=" ")                  
        for j in range(1,i+1):
            print(j, end=" ")
        print("")
pattern4()
print("")
