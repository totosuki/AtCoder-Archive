Q = int(input())
D = dict()
for i in range(Q):
  q = input()
  if q[0]=="1":
    X=int(q.split()[1])
    D[X]=D.get(X,0)+1
  elif q[0]=="2":
    X=int(q.split()[1])
    D[X]-=1
    if D[X]==0:
      del D[X]
  else:
    print(len(D))