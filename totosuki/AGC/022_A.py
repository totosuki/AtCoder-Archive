import string
alphabet = string.ascii_lowercase
S = input()

if len(S) != 26:
  rslt = []
  for a in alphabet:
    if a not in S:
      rslt.append(a)
  print(S + rslt[0])
else:
  del_char = []
  for i in reversed(range(1,26)):
    del_char.append(S[i])
    del_char.sort()
    for j in range(len(del_char)):
      rslt = S[:i-1] + del_char[j]
      if "".join(rslt) > S:
        print(*rslt, sep = "")
        exit()
  print(-1)