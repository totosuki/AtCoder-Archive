S = [input() for _ in range(10)]
S_nodupe = list(set(S))
sharp_line = ""
for i in range(len(S_nodupe)):
  if "#" in S_nodupe[i]:
    sharp_line = "".join(S_nodupe[i])

A = B = C = D = 0

#find A
for i in range(len(S)):
  if S[i] == sharp_line:
    A = i + 1
    break
#find B
for i in reversed(range(len(S))):
  if S[i] == sharp_line:
    B = i + 1
    break
#find C
C = sharp_line.find("#") + 1
#find D
D = sharp_line.rfind("#") + 1

print(A, B)
print(C, D)