import string
S = input()
alphabet = string.ascii_uppercase
collect = 0

if len(S) != 8:
  print("No")
  exit()

s1 = S[0]
s2 = S[1:-1]
s3 = S[-1]

if s1 in alphabet and s3 in alphabet:
  collect += 2

for s in s2:
  if s in alphabet:
    break
else:
  if 100000 <= int(s2) <= 999999:
    collect += 1

if collect == 3:
  print("Yes")
else:
  print("No")