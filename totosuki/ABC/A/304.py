N = int(input())
S = []
A = []
for i in range(N):
  s, a = input().split()
  S.append([s, int(a)])
  A.append(int(a))
index = A.index(min(A))
for i in range(N):
  i += index
  if i < N:
    print(S[i][0])
  else:
    print(S[i - N][0])