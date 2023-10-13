n = int(input())
x = list(map(int,input().split()))
s=0
k=0
for i in range(len(x)):
    if(i%2==0):
        s=s+x[i]
    if(i%2!=0):
        k=k+x[i]
d=s-k
print(d)