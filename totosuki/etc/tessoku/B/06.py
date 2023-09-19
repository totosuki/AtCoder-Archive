N = int(input())
A = [0] + list(map(int, input().split()))
Q = int(input())

cum = [[0]*2 for _ in range(100005)]

for i in range(1, N+1):
  cum[i] = cum[i-1]
  if A[i] == 1: cum[i][0] += 1
  if A[i] == 0: cum[i][1] += 1

for _ in range(Q):
  L, R = map(int, input().split())
  hit = cum[R][0] - cum[L-1][0]
  miss = cum[R][1] - cum[L-1][1]
  
  print("win" if hit > miss else "lose" if hit < miss else "draw")