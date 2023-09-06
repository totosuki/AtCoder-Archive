N, D = map(int, input().split())
T = list(map(int, input().split()))
for i in range(N - 1):
  if T[i+1] - T[i] <= D:
    print(T[i+1])
    exit()
print(-1)