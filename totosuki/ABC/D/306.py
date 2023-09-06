N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 2] * (3 * 10**5)

for i in range(1, N):
  dp[i][0] = -10**9 - 5
  dp[i][1] = -10**9 - 5

for i in range(N-1):
  if data[i][0] == 0:
    dp[i+1][0] = max([dp[i][0], max([dp[i][0], dp[i][1]]) + data[i][1]])
  else:
    dp[i+1][1] = max(dp[i][1], dp[i][0] + data[i][1])
  
  dp[i+1][0] = max(dp[i+1][0], dp[i][0])
  dp[i+1][1] = max(dp[i+1][1], dp[i][1])

print()

# conditions = [data[i][0] for i in range(len(data))]
# group = [(k,list(i)) for k, i in itertools.groupby(conditions)]
# group = [list(data) for data in group]
# print(group)
# scores = []
# i = 0
# flag = False

# while i < N:
#   if data[i][0] == 0 and data[i][0] >= 0:
#     scores.append(data[i][1])
#   elif data[i][0] == 1:
#     tmp = []
#     while data[i][0] == 1:
#       tmp.append(data[i][1])
#       i += 1
#       if i >= N:
#         flag = True
#         break
#     tmp2 = []
#     if not flag:
#       while data[i][0] == 0:
#         tmp2.append(data[i][1])
#         i += 1
#         if i >= N:
#           flag = True
#           break
#     maxtmp = max(tmp)
#     if tmp2:
#       maxtmp = maxtmp + max(tmp2)
#     scores.append(maxtmp)

#   i += 1
# print(scores)