n = int(input())
x = list(map(int,input().split()))
s=0
k=0
for i in range(len(x)):
    if(x[i]%2==0):
        s=s+x[i]
    if(x[i]%2!=0):
        k=k+x[i]
d=abs(s-k)
print(d)