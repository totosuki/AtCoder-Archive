import collections
S = list(input())
C = collections.Counter(S)
X = [0]*len(S)
for i in C.values():
  X[i-1] += 1
print("Yes" if all([i==0 or i==2 for i in X]) else "No")