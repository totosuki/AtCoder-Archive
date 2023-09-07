n,k = map(int, input().split())
cnt = 0
for i in range(n):
    for l in range(k):
        cnt = cnt + (i+1)*100
        cnt = cnt + l+1
print(cnt)