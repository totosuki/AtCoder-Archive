A, B = map(int, input().split())
if (A+B) % 2:
  print("IMPOSSIBLE")
  exit()
ave = (A + B) // 2
print(ave)