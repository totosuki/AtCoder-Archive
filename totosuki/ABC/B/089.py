N = int(input())
S = list(input().split())
rslt = "Three"

for i in range(N):
  if S[i] == "Y":
    rslt = "Four"

print(rslt)