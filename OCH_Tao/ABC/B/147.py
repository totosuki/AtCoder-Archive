S = input()
X = S[::-1]
cnt = 0
for i in range(len(S)):
  if S[i]!=X[i]:
    cnt+=1
print(cnt//2)