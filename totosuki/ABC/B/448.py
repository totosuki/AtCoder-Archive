N, M = map(int, input().split())
C = list(map(int, input().split()))
ans = 0

for _ in range(N):
    a, b = map(int, input().split())
    x = min(C[a-1], b)
    C[a-1] -= x
    ans += x

print(ans)
