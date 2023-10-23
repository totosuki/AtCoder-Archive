import string

A = string.ascii_uppercase
a = string.ascii_lowercase

S = input()
S_set = set(S)
cnt = 0

if len(S_set) == len(S):
  cnt += 1

flag = False
for s in S:
  if s in string.ascii_uppercase:
    flag = True
if flag:
  cnt += 1

flag = False
for s in S:
  if s in a:
    flag = True
if flag:
  cnt += 1

if cnt == 3:
  print("Yes")
else:
  print("No")