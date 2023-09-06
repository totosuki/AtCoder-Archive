a, b, c = map(int, input().split())
sort_list = sorted([a, b, c])
if sort_list[1] == b:
  print("Yes")
else:
  print("No")