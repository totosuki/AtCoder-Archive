N = int(input())
l = []
for i in range(N):
  l.append(int(input()))
l.sort(reverse=True)
X = l[0]
for i in range(N):
  if X != l[i]:
    Y = l[i]
    break
print(Y)