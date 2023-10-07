from collections import defaultdict

N = int(input())
S = [list(input()) for _ in range(N)]

win = defaultdict(int)

for i in range(N):
  win[i+1] = S[i].count("o")

dic2 = dict(sorted(win.items(), key=lambda x:-x[1]))

print(*dic2.keys())