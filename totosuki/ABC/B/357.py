import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

S = list(input())

lower_cnt = 0
upper_cnt = 0

for s in S:
  if s in lower:
    lower_cnt += 1
  elif s in upper:
    upper_cnt += 1

if lower_cnt > upper_cnt:
  print(''.join([s.lower() for s in S]))
else:
  print(''.join([s.upper() for s in S]))