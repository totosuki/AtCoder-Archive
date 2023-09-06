import string
alphabet = string.ascii_uppercase
N = int(input())
S = input()
rslt = ""

for s in S:
  i = alphabet.index(s)
  i += N
  rslt += alphabet[i % 26]

print(rslt)