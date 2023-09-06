S = input()
a_pos = -1
z_pos = -1
for i in range(len(S)):
  if S[i] == "A":
    a_pos = i
    break
for i in reversed(range(len(S))):
  if S[i] == "Z":
    z_pos = i
    break

print(z_pos - a_pos + 1)