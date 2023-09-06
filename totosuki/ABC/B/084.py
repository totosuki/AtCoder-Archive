A, B = map(int, input().split())
S = input()
rslt = "Yes"

for i in range(A):
  if S[i] in "0123456789":
    continue
  else:
    rslt = "No"
if S[A] != "-":
  rslt = "No"
for i in range(B):
  if S[-1 * i] in "0123456789":
    continue
  else:
    rslt = "No"

print(rslt)