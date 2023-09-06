N = int(input())
D = list(map(int, input().split()))
rslt = 0

for i in range(N):
  for j in range(i+1, N):
    rslt += D[i] * D[j]

print(rslt)