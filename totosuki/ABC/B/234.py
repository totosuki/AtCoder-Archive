import sys, itertools, math
input = sys.stdin.buffer.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
rslt = list()

for l in itertools.combinations(data, 2):
  x1, y1 = l[0]
  x2, y2 = l[1]
  dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  rslt.append(dist)

print(max(rslt))