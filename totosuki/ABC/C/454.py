from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

q = deque([1])
get = [False] * (N+1)
get[1] = True

while q:
    nexts = q.popleft()

    for next in G[nexts]:
        if not get[next]:
            get[next] = True
            q.append(next)

cnt = 0
for i in range(N+1):
    if get[i]: cnt += 1

print(cnt)
