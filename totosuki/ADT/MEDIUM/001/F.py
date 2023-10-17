N = int(input())
S = input()
angle = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
rec = {(0,0)}
pos = (0,0)
answer = "No"

for s in S:
  a = angle[s]
  x, y = pos
  n_x, n_y = a
  x += n_x
  y += n_y
  pos = (x, y)
  
  if pos in rec:
    answer = "Yes"
  
  rec.add(pos)

print(answer)