from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

sm = []
for key in cnt.keys():
    sm.append(key * cnt[key])
sm.sort(reverse=True)

for i in range(min(len(sm), K)):
    sm[i] = 0

print(sum(sm))
