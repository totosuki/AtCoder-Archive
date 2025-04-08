S = input()
cnt = 0
i = 0
while i < len(S):
  if S[i] == "0" and i != len(S)-1:
    if S[i+1] == "0":
      i += 1
  cnt += 1
  i += 1
print(cnt)
