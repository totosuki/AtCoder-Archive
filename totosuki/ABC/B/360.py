S, T = input().split()
S = list(S)
T = T
ans = "No"

for skip in range(1, len(S)-1):
  l = []
  for i in range(0,len(S), skip):
    l.append("".join(S[i:i+skip]))

  for c in range(1, skip+1):
    name = ""
    for i in range(len(l)):
      if len(l[i]) >= c:
        name += l[i][c-1]
    if name == T:
      ans = "Yes"

print(ans)