S = input()
T = input()
cnt = 0

for s, t in zip(S, T):
  cnt += 1
  if s != t: break
else:
  cnt += 1

print(cnt)