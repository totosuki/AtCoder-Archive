N = int(input())
S = list(map(int, input().split()))
rslt = []

for i in range(len(S)):
  if i == 0:
    rslt.append(S[i])
    continue

  rslt.append(S[i] - S[i-1])

print(*rslt)