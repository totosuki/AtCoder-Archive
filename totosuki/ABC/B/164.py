A, B, C, D = map(int, input().split())
t_cnt = -(-C // B)
a_cnt = -(-A // D)

if t_cnt <= a_cnt:
  print("Yes")
else:
  print("No")