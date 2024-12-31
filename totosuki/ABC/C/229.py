N, W = map(int, input().split())
cheese = []
for _ in range(N):
    A, B = map(int, input().split())
    cheese.append((A, B))

cheese.sort(reverse = True)
ans = 0
cnt = 0

for i in range(N):
    A, B = cheese[i]
    if cnt + B <= W:
        ans += A * B
        cnt += B
    else:
        ans += A * (W - cnt)
        break

print(ans)