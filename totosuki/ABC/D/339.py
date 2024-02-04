from collections import deque

def bfs(grid, start1, start2):
  N = len(grid)
  queue = deque([(start1, start2, 0)])  # ((player1 position), (player2 position), steps)
  seen1 = [[False] * N for _ in range(N)]
  seen2 = [[False] * N for _ in range(N)]
  seen1[start1[0]][start1[1]] = True
  seen2[start2[0]][start2[1]] = True
  
  while queue:
    (x1, y1), (x2, y2), steps = queue.popleft()
    
    if (x1, y1) == (x2, y2):
      return steps
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx1, ny1 = x1 + dx, y1 + dy
      nx2, ny2 = x2 + dx, y2 + dy
      
      move1 = 0 <= nx1 < N and 0 <= ny1 < N and grid[nx1][ny1] != '#' and not seen1[nx1][ny1]
      move2 = 0 <= nx2 < N and 0 <= ny2 < N and grid[nx2][ny2] != '#' and not seen2[nx2][ny2]
      
      if move1 or move2:
        if not move1:
          nx1, ny1 = x1, y1
        else:
          seen1[nx1][ny1] = True
          
        if not move2:
          nx2, ny2 = x2, y2
        else:
          seen2[nx2][ny2] = True
          
        queue.append(((nx1, ny1), (nx2, ny2), steps + 1))

  return -1

def solve(grid):
  N = len(grid)
  positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']
  return bfs(grid, positions[0], positions[1])

N = int(input())
grid = [input() for _ in range(N)]

print(solve(grid))