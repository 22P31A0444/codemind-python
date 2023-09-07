n = int(input())
p=0
while(n!=0):
    s=n%10
    p=p*10+s
    n=n//10
print(p)