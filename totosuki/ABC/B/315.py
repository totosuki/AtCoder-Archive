M = int(input())
D = list(map(int, input().split()))
D_sum = sum(D)
D_mid = (D_sum+1) // 2

day_cnt = 0
for i in range(M):
  for d in range(1,D[i]+1):
    day_cnt += 1
    if day_cnt == D_mid:
      print(i+1, d)
      exit()