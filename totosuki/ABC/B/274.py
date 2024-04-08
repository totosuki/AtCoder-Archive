H, W = map(int, input().split())
col = [0] * W

for i in range(H):
    C = list(input())
    for i in range(W):
        col[i] += (C[i] == "#")

print(*col)