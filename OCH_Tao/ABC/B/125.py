N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
diff = []
for i in range(N):
  if (X:=V[i]-C[i])>0:
    diff.append(X)
print(sum(diff))