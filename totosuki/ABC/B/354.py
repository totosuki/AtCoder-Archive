N = int(input())
S = []
C = []

for _ in range(N):
  s, c = input().split()
  S.append(s)
  C.append(int(c))

sm = sum(C)

S.sort()

print(S[sm % N])