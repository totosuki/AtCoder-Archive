import sys, itertools
input = sys.stdin.buffer.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

rslt_ab = 10**6
rslt_sm = 10**7

for combo in itertools.combinations(data, 2):
  rslt_ab = min(rslt_ab, max(combo[0][0], combo[1][1]))
  rslt_ab = min(rslt_ab, max(combo[0][1], combo[1][0]))

for d in data:
  rslt_sm = min(rslt_sm, d[0]+d[1])

print(min(rslt_ab, rslt_sm))