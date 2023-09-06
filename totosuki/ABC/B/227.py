import sys
input = sys.stdin.buffer.readline

N = int(input())
S = list(map(int, input().split()))
cnt = 0

for s in S:
  for a in range(1, 200):
    for b in range(1, 300):
      rslt = 4*a*b + 3*a + 3*b
      if rslt == s:
        break
    else:
      continue
    break
  else:
    cnt += 1

print(cnt)