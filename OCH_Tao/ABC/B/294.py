from string import ascii_uppercase
S = "."+ascii_uppercase
ans = ""
H, W = map(int, input().split())
for i in range(H):
  A = list(map(int, input().split()))
  ans += "".join(map(lambda x: S[x], A))+"\n"
print(ans, end="")
