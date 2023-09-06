N, K = map(int, input().split())
S = input()
j = 0
for i in range(len(S)):
  if "o" in S[i]:
    K -= 1
    if K == 0:
      print(S[:i+1] + S[i+1:].replace("o", "x"))
      break