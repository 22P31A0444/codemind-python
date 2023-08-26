n = int(input())
sum=0
for i in range(1,n,1):
    b=n%i
    if(b==0):
        sum=sum+i
if(n==sum):
    print("True")
else:
    print("False")
            