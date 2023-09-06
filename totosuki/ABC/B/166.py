N, K = map(int, input().split())
se = set()

for i in range(K):
  d = int(input())
  se = se | set(map(int, input().split()))

print(N - len(se))