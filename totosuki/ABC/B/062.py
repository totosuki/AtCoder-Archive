H, W = map(int, input().split())
fig = [["#"]*(W+2) for _ in range(H+2)]

for i in range(1, H+1):
  a = list(input())
  for j in range(1, W+1):
    fig[i][j] = a[j-1]

[print("".join(f)) for f in fig]