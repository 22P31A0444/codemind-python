n =int(input())
a=0;b=1
c=a+b
while(c<=n):
    a=b
    b=c
    c=a+b
if(c-n<n-b):
    print(c)
elif(c-n>n-b):
    print(b)
else:
    print(b,c)