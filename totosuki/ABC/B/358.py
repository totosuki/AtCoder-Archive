N, A = map(int, input().split())
T = list(map(int, input().split()))

time = 0
ans = []

for i in range(N):
  if time <= T[i]:
    time = T[i] + A
    ans.append(time)
  else:
    time += A
    ans.append(time)

print(*ans, sep = "\n")