abc = "abcdefgh"
nums = "87654321"
S = []
for i in range(8):
  s = input()
  for j in range(8):
    if s[j] == "*":
      print(abc[j] + nums[i])