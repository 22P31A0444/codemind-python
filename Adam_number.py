n = int(input())
s=n*n
p=0
g=0
while(n!=0):
    d = n%10
    p = p*10+d
    n = n//10
k = p*p
while(k!=0):
    l=k%10
    g=g*10+l
    k=k//10
if(g==s):
    print("True")
else:
    print("False")