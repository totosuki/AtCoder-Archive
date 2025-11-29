from collections import defaultdict

N, M = map(int, input().split())

d = defaultdict(list)

for _ in range(N):
    A, B = map(int, input().split())
    d[A].append(B)

for i in range(1, M+1):
    print(sum(d[i]) / len(d[i]))
