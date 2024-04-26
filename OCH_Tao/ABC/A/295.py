N = int(input())
W = input().split()
if "and" in W:
  print("Yes")
elif "not" in W:
  print("Yes")
elif "that" in W:
  print("Yes")
elif "the" in W:
  print("Yes")
elif "you" in W:
  print("Yes")
else:
  print("No")