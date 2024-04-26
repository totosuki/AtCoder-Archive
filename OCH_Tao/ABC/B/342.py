N = int(input())
P = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
  A,B = map(int,input().split())
  for j in P:
    if j == A:
      print(A)
      break
    elif j == B:
      print(B)
      break
    else:
      continue