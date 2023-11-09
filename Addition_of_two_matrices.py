n = int(input())
s = [list(map(int,input().split())) for i in range(n)]
k = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        s[i][j] = s[i][j]+k[i][j]
for i in s:
    for j in i:
        print(j,end=' ')
    print()