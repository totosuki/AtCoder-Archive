N = int(input())
table = [[0 for l in range(100)] for i in range(100)]
cnt = 0
for i in range(N):
    a,b,c,d = map(int,input().split())
    for l in range(a,b):
        for k in range(c,d):
            table[l][k] = 1
for i in table:
    for l in i:
        if l == 1:
            cnt = cnt +1
print(cnt)