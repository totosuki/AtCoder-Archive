from collections import defaultdict

N = int(input())
S = list(input())
Q = int(input())

shape = 0
d = defaultdict(str)

for _ in range(Q):
  t, x, c = input().split()
  t = int(t)
  x = int(x)
  if t == 1:
    S[x-1] = c
    d[x-1] = c
  elif t == 2:
    shape = 1
    d = defaultdict(str)
  else:
    shape = 2
    d = defaultdict(str)

S = "".join(S)
if shape == 1:
  S = S.lower()
elif shape == 2:
  S = S.upper()

S = list(S)
for x in d.keys():
  S[x] = d[x]

print("".join(S))