n = int(input())
q=n
p=0
while(q!=0):
    s=q%10
    p=p*10+s
    q=q//10
if(p==n):
    print("True")
else:
    print("False")