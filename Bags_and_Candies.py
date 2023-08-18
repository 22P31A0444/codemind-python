n,k,m = map(int,input().split())
a = k*m
if(n%a==0):
    print(n//a)
elif(n%a!=0):
    print((n//a)+1)