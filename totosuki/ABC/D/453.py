from collections import deque

H, W = map(int, input().split())
S = [input() for i in range(H)]

for i, row in enumerate(S):
    for j, c in enumerate(row):
        if c == "S":
            si, sj = i, j
        elif c == "G":
            gi, gj = i, j

q = deque()
INF = 1 << 60
dist = [[[INF]*W for _ in range(H)] for _ in range(4)]
ds = "RDLU"
dij = [(0,1), (1,0), (0,-1), (-1,0)]

for di in range(4):
    dist[di][si][sj] = 0
    q.append((di, si, sj))

prev = [[[None]*W for _ in range(H)] for _ in range(4)]

while q:
    tdi, i, j = q.popleft()

    if (i, j) == (gi, gj):
        print("Yes")
        ans = []
        while prev[tdi][i][j] is not None:
            ans.append(ds[tdi])
            i,j,tdi = prev[tdi][i][j]
        ans.reverse()
        print("".join(ans))
        exit()

    for ndi,(di,dj) in enumerate(dij):
        ni,nj = i+di, j+dj
        if not 0 <= ni < H: continue
        if not 0 <= nj < W: continue
        if S[ni][nj] == "#": continue
        if S[i][j] == "o" and tdi != ndi: continue
        if S[i][j] == "x" and tdi == ndi: continue
        if dist[tdi][i][j] + 1 < dist[ndi][ni][nj]:
            dist[ndi][ni][nj] = dist[tdi][i][j] + 1
            q.append((ndi,ni,nj))
            prev[ndi][ni][nj] = (i,j,tdi)

print("No")
