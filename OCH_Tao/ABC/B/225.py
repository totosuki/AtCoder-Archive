N = int(input())
D = dict()
for i in range(N-1):
  A,B = map(int,input().split())
  D[A]=D.get(A,0)+1
  D[B]=D.get(B,0)+1
print("Yes" if max(D.values())==N-1 and len(D)==N else "No")