num = int(input("Enter a value:"))  
temp = num  
sum = 0  
while(num > 0):
    dig = (num%10)  
    sum = (sum * 10) + dig  
    num = num//10   

if(sum == temp):
    print("This is a palindrome number!")  
else:  
    print("This is not a palindrome number!") 