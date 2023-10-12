n  = int(input())
x = list(map(int,input().split()))
s=0
for i in range(1,len(x),2):
    s=s+x[i]
print(s)