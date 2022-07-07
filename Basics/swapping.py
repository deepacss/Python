
#Swapping between two numbers

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Original values:",a,b)

temp=b
b=a
a=temp
print("Swapping values:", a,b)
