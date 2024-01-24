N = int(input())
T = 0
A = 0
for i in range(N):
  x,y = map(int,input().split())
  T += x
  A += y
if T>A:
  print("Takahashi")
elif T==A:
  print("Draw")
else:
  print("Aoki")