N, M = map(int, input().split())
S = list(input())

canT = M
canlogoT = 0
logoT = 0

for i in range(N):
  if S[i] == "0":
    canT = M
    canlogoT = logoT
  if S[i] == "1":
    if canT > 0:
      canT -= 1
    else:
      if canlogoT > 0:
        canlogoT -= 1
      else:
        logoT += 1
  if S[i] == "2":
    if canlogoT > 0:
      canlogoT -= 1
    else:
      logoT += 1

print(logoT)