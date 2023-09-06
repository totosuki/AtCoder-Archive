N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cum = [[0]*2 for _ in range(100005)]

for i in range(1, N+1):
  if A[i-1] == 1:
    cum[i][0] = cum[i-1][0] + 1
    cum[i][1] = cum[i-1][1]
  else:
    cum[i][0] = cum[i-1][0]
    cum[i][1] = cum[i-1][1] + 1

for _ in range(Q):
  L, R = map(int, input().split())
  hit = cum[R][0] - cum[L-1][0]
  miss = cum[R][1] - cum[L-1][1]
  
  if hit > miss:
    print("win")
  elif hit < miss:
    print("lose")
  else:
    print("draw")