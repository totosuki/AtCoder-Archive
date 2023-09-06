A, B = map(int, input().split())
nums = list(range(2, 14)) + [1]
if nums.index(A) > nums.index(B):
  print("Alice")
elif nums.index(A) < nums.index(B):
  print("Bob")
else:
  print("Draw")