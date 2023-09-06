import sys, string
input = sys.stdin.buffer.readline

ABC = string.ascii_lowercase
S = input().decode().strip()
T = input().decode().strip()
answer = "Yes"

fst_S = ABC.index(S[0])
fst_T = ABC.index(T[0])
if fst_S <= fst_T:
  skip = fst_T - fst_S
else:
  skip = (26-fst_S) + fst_T

i = 0
while i < len(S):
  tmp = (ABC.index(S[i]) + skip) % 26
  if ABC[tmp] != T[i]:
    answer = "No"
  i += 1

print(answer)