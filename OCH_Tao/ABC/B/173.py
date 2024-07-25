N = int(input())
D = {"AC":0,"WA":0,"TLE":0,"RE":0}
for i in range(N):
  S = input()
  D[S]=D[S]+1
for i in D:
  print(f"{i} x {D[i]}")