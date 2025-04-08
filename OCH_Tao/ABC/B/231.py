N = int(input())
D = dict()
for i in [0]*N:
  S = input()
  D[S]=D.get(S,0)+1
print(max(D,key=D.get))