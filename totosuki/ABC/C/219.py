import sys, string
input = sys.stdin.buffer.readline
alpha = string.ascii_lowercase

X = input().decode().strip()
N = int(input())
rslt = []

for i in range(N):
  S = input().decode().strip()
  S_n = []
  for s in S:
    s_i = X.index(s)
    S_n.append(alpha[s_i])
  rslt.append([S, "".join(S_n)])

rslt.sort(key = lambda s: s[1])

[print(r[0]) for r in rslt]