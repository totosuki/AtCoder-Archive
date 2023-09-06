S = input()
if len(S) % 2:
  S1 = S[:len(S)//2]
  S2 = S[len(S)//2 +1:]
else:
  S1 = S[:len(S)//2]
  S2 = S[len(S)//2:]

cnt = 0
for s1, s2 in zip(S1, reversed(S2)):
  if s1 != s2:
    cnt += 1

print(cnt)