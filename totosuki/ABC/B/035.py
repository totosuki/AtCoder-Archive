S = input()
T = int(input())

q_cnt = S.count("?")
pos = [0,0]

for s in S:
  if s == "L":
    pos[0] -= 1
  elif s == "R":
    pos[0] += 1
  elif s == "U":
    pos[1] += 1
  elif s == "D":
    pos[1] -= 1

if T == 1:
  print(abs(pos[0]) + abs(pos[1]) + q_cnt)
elif T == 2:
  dist = abs(pos[0]) + abs(pos[1])
  if q_cnt <= dist:
    print(dist - q_cnt)
  else:
    if (q_cnt - dist) % 2 == 1:
      print(1)
    else:
      print(0)