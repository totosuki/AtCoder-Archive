N, M = map(int, input().split())
S = input()
T = input()

ans = 3

if T[:N] == S and T[-N:] == S:
  ans = 0
elif T[:N] == S:
  ans = 1
elif T[-N:] == S:
  ans = 2

print(ans)