R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]
B_poses = []
clean_poses = []
for row in range(R):
  for col in range(C):
    if M[row][col] not in ".#":
      B_poses.append([row, col])

for B_pos in B_poses:
  b_power = int(M[B_pos[0]][B_pos[1]])
  clean_poses.append(B_pos)
  while b_power >= 1:
    for p in range(0, b_power + 1):
      x_plus = B_pos[0] + p
      x_minus = B_pos[0] - p
      y_plus = B_pos[1] + (b_power - p) 
      y_minus = B_pos[1] - (b_power - p) 
      if x_plus < R and y_plus < C:
        clean_poses.append([x_plus, y_plus])
      if x_minus >= 0 and y_plus < C:
        clean_poses.append([x_minus, y_plus])
      if x_minus >= 0 and y_minus >= 0:
        clean_poses.append([x_minus, y_minus])
      if x_plus < R and y_minus >= 0:
        clean_poses.append([x_plus, y_minus])
    b_power -= 1

clean_poses = list(map(list, set(map(tuple, clean_poses))))

for pos in clean_poses:
  M[pos[0]][pos[1]] = "."
for m in M:
  print("".join(m))