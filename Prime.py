n = int(input())
c=0
for i in range(1,n+1):
    k=n%i
    if(k==0):
        c += 1
if(c==2):
    print("Prime")
else:
    print("Not Prime")