import string
S = list(input())
l = list(string.ascii_lowercase)
for i in S:
  if i in l:
    l.remove(i)
try:
  print(l[0])
except IndexError:
  print("None")