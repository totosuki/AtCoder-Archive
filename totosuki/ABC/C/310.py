import sys
input = sys.stdin.buffer.readline

N = int(input())
se = set()

for _ in range(N):
  S = list(input().decode().strip())
  s = "".join(S)
  r_s = "".join(reversed(S))

  if not s in se and not r_s in se:
    se.add(s)

print(len(se))