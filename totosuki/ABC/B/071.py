import string
alphabet = set(string.ascii_lowercase)
S = input()

for s in S:
  alphabet.discard(s)

if not alphabet:
  print("None")
  exit()

rslt = sorted(list(alphabet))
print(rslt[0])