N, Q = map(int, input().split())
T = list(map(int, input().split()))
ha = [True] * N

for t in T:
  t -= 1
  ha[t] = not ha[t]

print(ha.count(True))