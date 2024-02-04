from numpy import base_repr

N = base_repr(int(input()) - 1, 5)

ns = str(N)
nums = ["0", "2", "4", "6", "8"]
answer = ""

for i in range(len(ns)):
  answer += nums[int(ns[i])]

print(answer)
