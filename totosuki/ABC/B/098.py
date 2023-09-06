N = int(input())
S = input()
rslt = []

for i in range(1, N):
  se = set(S[:i]) & set(S[i:])
  rslt.append(len(se))

print(max(rslt))