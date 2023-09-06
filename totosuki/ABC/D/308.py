from collections import deque
H, W = map(int, input().split())
S = [input() for _ in range(H)]
snuke = "snuke" * 20005

if S[0][0] != "s":
  print("No")
  exit()

queue = deque([[0,0,0]])
while len(queue) != 0:
  print(f"queue: {queue}, next_pos: {queue[0]}")  

  next_pos = queue.pop()
  
  if next_pos[:2] == [H-1,W-1]:
    print("Yes")
    exit()
  
  cnt = next_pos[2]
  
  if S[next_pos[0]][next_pos[1]] == snuke[cnt]:
    li = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    cnt += 1
    for l in li:
      near_pos = [0,0]
      near_pos[0] = next_pos[0] + l[0]
      near_pos[1] = next_pos[1] + l[1]
      if 0 <= near_pos[0] < H and 0 <= near_pos[1] < W:
        if S[near_pos[0]][near_pos[1]] == snuke[cnt]:
          queue.append([near_pos[0], near_pos[1], cnt])
print("No")