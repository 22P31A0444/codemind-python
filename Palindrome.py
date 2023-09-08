n = int(input())
p=0
q=n
while(q!=0):
    s=q%10
    p=p*10+s
    q=q//10
if(p==n):
    print("Palindrome")
else:
    print("Not Palindrome")
    