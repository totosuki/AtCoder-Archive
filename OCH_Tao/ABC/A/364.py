N = int(input())
cnt = False
X = False
S = []
for i in range(N):
  S.append(input())
for i in S:
  if X:
    print("No")
    break
  elif cnt and i=="sweet":
    X=True
  elif i=="sweet":
    cnt=True
  else:
    cnt=False
else:
  print("Yes")