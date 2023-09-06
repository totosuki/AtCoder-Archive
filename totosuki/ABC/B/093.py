A, B, K = map(int, input().split())

if K > B-A+1:
  K = B-A+1

nums = list(range(A,A+150)) + list(range(B-150, B+1))
nums = [i for i in nums if i >= 1]
nums = list(set(nums[:K] + nums[-1*K:]))
nums.sort()

print(*nums, sep = "\n")