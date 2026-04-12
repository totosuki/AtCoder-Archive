import sys
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())
tile = [list(input()) for _ in range(H)]

# [U, R, D, L]
seen = [[[False]*4 for _ in range(W)] for _ in range(H)]
sy = sx = 0
vec = [("U",-1,0),("R",0,1),("D",1,0),("L",0,-1)]

def dfs(now, route):
    ny, nx, ri = now
    is_o = tile[ny][nx] == "o"
    is_x = tile[ny][nx] == "x"

    if route:
        if not is_o and not is_x:
            seen[ny][nx] = [True]*4
        else:
            seen[ny][nx][ri] = True
    else:
        seen[ny][nx] = [True]*4


    if tile[ny][nx] == "G": return [route]

    
    for i in range(4):
        v, dy, dx = vec[i]
        nxty, nxtx = ny+dy, nx+dx
        
        if not (0 <= nxty < H and 0 <= nxtx < W): continue
        if seen[nxty][nxtx][i]: continue
        if is_o and route != v: continue
        if is_x and route == v: continue
        if tile[nxty][nxtx] == "#": continue
        
        if ans := dfs((nxty, nxtx, i), v):
            ans.append(route)
            return ans
    
    return []


# start を探す
for i in range(H):
    for j in range(W):
        if tile[i][j] == "S":
            sy = i; sx = j
            break
    else:
        continue
    break

ans = dfs((sy, sx, -1), None)
ans.reverse()
if ans:
    print("Yes")
    print(*ans[1:], sep="")
else:
    print("No")

# 各マスの出発した向きを保存