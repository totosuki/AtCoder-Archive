W = list(input())
X = list(set(W))
for i in X:
  if W.count(i)%2!=0:
    print("No")
    break
else:
  print("Yes")