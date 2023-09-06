N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
say_ptn = set()
for s in S:
  say_ptn.add(s)
for t in T:
  say_ptn.add(t)

rslt = []
say_ptn = list(say_ptn)

for i in range(len(say_ptn)):
  cnt = 0
  for s in S:
    if say_ptn[i] == s:
      cnt += 1
  for t in T:
    if say_ptn[i] == t:
      cnt -= 1
  rslt.append(cnt)

print(max(0, max(rslt)))