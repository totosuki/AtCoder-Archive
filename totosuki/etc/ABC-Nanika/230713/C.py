import sys
input = sys.stdin.buffer.readline

N = int(input())
S = [input().decode().strip() for _ in range(N)]
se = set()

for s in S:
  if s[0] != "!":
    if "!" + s in se:
      print(s)
      exit()
    se.add(s)
  else:
    if s[1:] in se:
      print(s[1:])
      exit()
    se.add(s)

print("satisfiable")