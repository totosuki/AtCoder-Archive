N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
D = []
ans = set()
for i in range(N):
  D.append({"A":A[i],"B":B[i],"N":i+1})
D.sort(key=lambda x:(x["A"],-x["N"]))
for i in range(X):
  ans.add(D.pop()["N"])
D.sort(key=lambda x:(x["B"],-x["N"]))
for i in range(Y):
  ans.add(D.pop()["N"])
D.sort(key=lambda x:(x["A"]+x["B"],-x["N"]))
for i in range(Z):
  ans.add(D.pop()["N"])
print(*sorted(ans),sep="\n")