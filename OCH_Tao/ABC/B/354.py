N = int(input())
D = dict()
for i in range(N):
  S,C = input().split()
  D[S]=int(C)
X = sorted(D.items(),key=lambda x:x[0])
print(X[sum(D.values())%N][0])