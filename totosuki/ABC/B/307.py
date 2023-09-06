N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    t = S[i] + S[j]
    t_r = "".join(list(reversed(t)))
    if t == t_r:
      print("Yes")
      exit()

print("No")