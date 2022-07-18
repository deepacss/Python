num = int(input("Enter a number:"))  
sum = 0  
sq=num*num
print("square of",num ,"is:",sq)
while(sq>0):
    rem = sq% 10
    sum = sum + rem
    sq =  sq// 10

print("Sum of the digits of square of the number: ",sum)
if(sum == num):
    print(num," is a Neon Number")
else:
    print(num," is not a Neon Number")
