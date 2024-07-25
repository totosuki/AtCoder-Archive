X,Y = map(int,input().split())
L = []
for i in range(X+1):
  L.append(2*i+4*(X-i))
print("Yes" if Y in L else "No")