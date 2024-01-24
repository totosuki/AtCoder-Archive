N = int(input())
A,B = map(int,input().split())
K = int(input())
P = list(map(int,input().split()))
P.append(A)
P.append(B)
if len(P) != len(set(P)):
  print("NO")
else:
  print("YES")