N = int(input())
S = [input() for _ in range(N)]
ans = "Yes"

for i in range(1, N-1):
  if S[i-1] == S[i] and S[i] == "sweet":
    ans = "No"

print(ans)