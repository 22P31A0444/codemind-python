n=int(input())
c=0
x = list(map(int,input().split()))
for i in range(1,n-1):
    if((x[i-1]%2==0 and x[i+1]%2!=0) or (x[i-1]%2!=0 and x[i+1]%2==0)):
        c=c+1
print(c)