N,X = input().split()
S = input().split()
n = 0
for i in S:
  if int(i) <= int(X):
    n += int(i)

print(n)