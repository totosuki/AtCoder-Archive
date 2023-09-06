T = int(input())
N = int(input())
B = [0] * (T+2)
cum = [0] * (T+1)

for i in range(N):
  L, R = map(int, input().split())
  B[L+1] += 1
  B[R+1] -= 1

for i in range(1, T+1):
  cum[i] = cum[i-1] + B[i]
  print(cum[i])