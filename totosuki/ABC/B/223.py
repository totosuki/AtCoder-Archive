import sys
input = sys.stdin.buffer.readline

S = input().decode().strip()
rslt = list()

if len(S) == 1:
  print(S, S, sep = "\n")
  exit()

for i in range(len(S)):
  S = S[1:] + S[0]
  rslt.append(S)

print(min(rslt), max(rslt), sep = "\n")