a = int(input("Enter the first number:"))  
b = int(input("Enter the second number:"))  
c = int(input("Enter the third number:"))  

#using Ternary operator to fing the biggest number
max= a if (a>b and a>c) else b if(b>a and b>c) else c
print("The biggest number is:",max)