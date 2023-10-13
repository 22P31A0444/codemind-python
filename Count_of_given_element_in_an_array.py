n = int(input())
x = list(map(int,input().split()))
z = int(input())
c=0
for i in range(len(x)):
    if(z==x[i]):
        c=c+1
print(c)