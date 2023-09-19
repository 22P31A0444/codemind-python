n = int(input())
temp=n
p=0
l=0
while n:
    s=n%10
    p=p*10+s
    n=n//10
i=1
while p:
    k=(p%10)**i
    l=l+k
    p=p//10
    i=i+1
if(l==temp):
    print("True")
else:
    print("False")