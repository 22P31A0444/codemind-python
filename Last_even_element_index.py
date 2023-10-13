n = int(input())
x = list(map(int,input().split()))
l = []
for i in range(len(x)):
    if(x[i]%2==0):
       l.append(i)
print(l[-1])