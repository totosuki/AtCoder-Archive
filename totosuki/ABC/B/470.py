N = int(input())
C = list(map(int, input().split()))
cnt = [0] * (N+1)

for i in range(N):
    cnt[C[i]] += 1

print(N - max(cnt))
