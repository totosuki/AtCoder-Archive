N = int(input())
X = 0
H = 0
for i in range(N):
  A,B = map(int,input().split())
  H = max(H,B-A)
  X+=A
print(X+H)