n =  int(input())
x = list(map(int,input().split()))
s = sum(x)//n
if(s in x):
    print("True")
else:
    print("False")