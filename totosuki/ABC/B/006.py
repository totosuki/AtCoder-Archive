n = int(input())
l = [0, 0, 1]
if n <= 3:
  print(l[n-1])
else:
  for i in range(3, n):
    tmp = (l[i-3] + l[i-2] + l[i-1]) % 10007
    l.append(tmp)
  print(l[n-1])

n = int(input())
l = [0, 0, 1]
if n <= 3:
  print(l[n-1])
else:
  for i in range(3, n):
    tmp = (l[i-3] + l[i-2] + l[i-1]) % 10007
    l.append(tmp)
  print(l[n-1])

# def fun(n) -> list:
#   dp = [0] * 4
#   dp[0] = 0
#   dp[1] = 0
#   dp[2] = 1

#   for _ in range(3, n):
#     dp[3] = dp[2] + dp[1] + dp[0]
#     dp[0] = dp[1]
#     dp[1] = dp[2]
#     dp[2] = dp[3]
#     dp[3] = 0

#   return dp