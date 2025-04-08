from collections import Counter
N = int(input())
L = []
X = []
for i in range(N):
  ST = list(set(input().split()))
  L.append(ST)
  X.extend(ST)
X = [i for i,j in Counter(X).items() if j<=1]
print("Yes" if all([i[0] in X or i[1] in X for i in L]) else "No")