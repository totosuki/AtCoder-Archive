S = input()

rslt = -1

for i in range(len(S)):
  for j in range(len(S)):
    s = S[i:j+1]
    reversed_s = s[::-1]
    if s == reversed_s:
      rslt = max(rslt, len(s))

print(rslt)