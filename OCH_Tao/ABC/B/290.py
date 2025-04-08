N, K = map(int, input().split())
S = input()
ans = ""
for i in range(N):
  if S[i] == "o" and K > 0:
    ans += "o"
    K -= 1
  else:
    ans += "x"
print(ans)
