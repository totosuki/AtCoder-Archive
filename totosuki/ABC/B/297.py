S = input()
B_indexes = [i for i, s in enumerate(S) if s == "B"]
R_indexes = [i for i, s in enumerate(S) if s == "R"]
K_index = S.index("K")

if (B_indexes[0] % 2 and B_indexes[1] % 2) or (not B_indexes[0] % 2 and not B_indexes[1] % 2):
  print("No")
  exit()

if R_indexes[0] < K_index < R_indexes[1]:
  print("Yes")
else:
  print("No")