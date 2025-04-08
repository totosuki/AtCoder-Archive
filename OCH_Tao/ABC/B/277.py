import re
N = int(input())
L = set()
R = re.compile(r"[HDCS][A23456789TJQK]")
for i in range(N):
  S = input()
  if re.fullmatch(R,S):
    L.add(S)
print("Yes" if len(L)==N else "No")