N,S,T = map(int,input().split())
W = int(input())
A = []
for i in range(N-1):
  A.append(int(input()))

X = [W]
now = W
for i in A:
  now += i
  X.append(now)

cnt = 0
for i in X:
  if S <= i <= T:
    cnt += 1

print(cnt)