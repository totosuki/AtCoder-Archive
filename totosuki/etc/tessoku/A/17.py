import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [0,0] + list(map(int, input().split()))
B = [0,0,0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[2] = A[2]

for i in range(3, N+1):
  dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])

place = N
rslt = []

while True:
  rslt.append(place)
  
  if place == 1:
    break
  
  if (dp[place-1] + A[place] == dp[place]):
    place -= 1
  else:
    place -= 2

rslt.reverse()

print(len(rslt))
print(*rslt)