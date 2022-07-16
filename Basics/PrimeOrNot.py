#To check whether the number is prime or not

n=int(input("Enter the value of n:"))
for i in range(2,n):
    if(n%i==0):
        print(n,"is not a pime number")
        break
else:
    print(n,"is a pime number")