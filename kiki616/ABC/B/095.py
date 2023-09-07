N,X = map(int,input().split())
M = []
cnt = 0
for i in range(N):
    m = int(input())
    M.append(m)
    X -= m
    cnt += 1

while True:
    if X >= min(M):
        X -= min(M)
        cnt += 1
    else:
        break
print(cnt)