import sys
input = sys.stdin.buffer.readline

N, M, H, K = map(int, input().split())
S = list(input().decode().rstrip())
heal_pos = {tuple(map(int, input().split())) for _ in range(M)}
pos = (0, 0)
hp = H
vec = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}
used = set()
rslt = "Yes"

for i in range(N):
  vx, vy = vec[S[i]]
  px, py = pos
  pos = (px+vx, py+vy)
  hp -= 1
  
  if hp < 0:
    rslt = "No"
    break
  else:
    if (pos in heal_pos) and (pos not in used) and (hp < K):
      used.add(pos)
      hp = max(K, hp)

print(rslt)
