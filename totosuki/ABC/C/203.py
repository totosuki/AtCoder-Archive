import sys, collections
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
pos = 0

money = collections.defaultdict(int)
for _ in range(N):
  A, B = map(int, input().split())
  money[A] += B

money = sorted(money.items())

for data in money:
  A, B = data
  dist = A-pos

  if K >= dist:
    K -= dist
    K += B
    pos += dist
  else:
    pos += K
    break
else:
  pos += K

print(pos)