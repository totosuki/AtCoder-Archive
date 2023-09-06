N, D = map(int, input().split())
S = [input() for _ in range(N)]
hima = list()

cnt = 0
for i in range(D):
  for j in range(N):
    if S[j][i] == "o":
      continue
    else:
      hima.append(cnt)
      cnt = 0
      break
  else:
    cnt += 1
else:
  hima.append(cnt)

print(max(hima))