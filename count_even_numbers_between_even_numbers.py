n = int(input())
x = list(map(int,input().split()))
c=0
for i in range(len(x)-2):
    if(x[i]%2==0 and x[i+2]%2==0):
        if(x[i+1]%2==0):
            c=c+1
print(c)