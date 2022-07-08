
n=int(input("Enter the value of n:"))
sum=0
copy=n
l=len(str(n))
while(n>0):
    rem=n%10
    sum=sum+rem**l
    n=n//10
if(copy==sum):
    print("The given number",copy, "is an amstrong number")
else:
     print("The given number",copy, " is not an amstrong number")



    