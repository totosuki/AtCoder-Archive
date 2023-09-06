s_sort = sorted(input())
t_sort = sorted(input(), reverse = True)
s_sort_len, t_sort_len = len(s_sort), len(t_sort)
flag = None

for s, t in zip(s_sort, t_sort):
  if s > t:
    flag = False
    break
  elif s < t:
    flag = True
    break
  else:
    continue

if flag is None and s_sort_len < t_sort_len:
  print("Yes")
elif flag is None and s_sort_len >= t_sort_len:
  print("No")
else:
  print("Yes") if flag else print("No")