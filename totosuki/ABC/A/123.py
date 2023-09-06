pos = [int(input()) for _ in range(5)]
k = int(input())
if pos[-1] - pos[0] <= k:
  print("Yay!")
else:
  print(":(")