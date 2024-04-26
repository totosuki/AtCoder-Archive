N = int(input())
S = list(input())
cnt = 0
for i in range(N):
  X = set(S[:i])
  Y = set(S[i:])
  cnt = max(len(list(X&Y)),cnt)
print(cnt)