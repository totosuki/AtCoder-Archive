import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

nums = {}
for i in range(N):
  nums[i] = A[i]

nums = sorted(nums.items(), key = lambda x: x[1])
rslt = {}
default = K//N
amari = K % N

for i, (k, _) in enumerate(nums):
  i += 1
  rslt[k] = default + 1 if i <= amari else default

rslt = sorted(rslt.items(), key = lambda x: x[0])

[print(v) for _, v in rslt]


# 定数倍の良い実装
N, K = map(int,input().split())
a = list(map(int,input().split()))

order = [(a[i] << 32) + i for i in range(N)]
order.sort()

answer = [K // N for i in range(N)]
for i in range(K % N):
  answer[order[i] & ((1 << 32) - 1)] += 1
for x in answer:
  print(x)
