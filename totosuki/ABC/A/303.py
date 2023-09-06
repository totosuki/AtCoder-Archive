N = int(input())
S = input()
T = input()
is_similar = True
for i in range(N):
  if S[i] != T[i]:
    if S[i] == "1" or S[i] == "l":
      if T[i] == "1" or T[i] == "l":
        continue
    if S[i] == "0" or S[i] == "o":
      if T[i] == "0" or T[i] == "o":
        continue
    is_similar = False
if is_similar:
  print("Yes")
else:
  print("No")