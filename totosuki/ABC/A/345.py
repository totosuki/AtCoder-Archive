S = input()
ans = "Yes"

if "<" != S[0]:
  ans  = "No"
if ">" != S[-1]:
  ans = "No"
if ">" in S[1:-1] or "<" in S[1:-1]:
  ans = "No"

print(ans)