N = int(input())
for_num = 0
for _ in range(N):
  message = input()
  if message == "For":
    for_num += 1
if for_num > N / 2:
  print("Yes")
else:
  print("No")