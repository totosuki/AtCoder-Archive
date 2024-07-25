A,B,C,D,E,F = map(int,input().split())
G,H,I,J,K,L = map(int,input().split())
X1 = set(range(A,D+1))
X2 = set(range(G,J+1))
Y1 = set(range(B,E+1))
Y2 = set(range(H,K+1))
Z1 = set(range(C,F+1))
Z2 = set(range(I,L+1))
if all([len(i)>1 for i in [X1&X2,Y1&Y2,Z1&Z2]]):
  print("Yes")
else:
  print("No")