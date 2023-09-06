import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

mx = 10**5+5
ok = [0 if i in B else 1 for i in range(mx)]
dp = [0] * (mx)
dp[0] = 1

for i in range(mx):
  if dp[i]:
    for a in A:
      if i+a >= mx: break
      dp[i+a] = 1 if ok[i+a] else 0

print("Yes") if dp[X] else print("No")

# TLE解
# se = set()
# se.add(0)
# rslt = "No"

# while len(se):
#   n_se = set()

#   for x in se:
#     for a in A:
#       step = x + a
#       if step in B: continue
#       if step > X: break
#       if step == X: rslt = "Yes"
#       n_se.add(step)
  
#   se = n_se

# print(rslt)