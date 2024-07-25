N = int(input())
S = set()
for i in range(1,10):
  for j in range(1,10):
    S.add(i*j)
print("Yes" if N in S else "No")