N, L, R = map(int, input().split())
S = input()
cnt = 0
a = ord("a")
data = [[0]*26 for _ in range(N)]

for i in range(N):
    s = ord(S[i])
    if i+L < N:   data[i+L][s-a] += 1
    if i+R+1 < N: data[i+R+1][s-a] -= 1

for i in range(1, N):
    for j in range(26):
        data[i][j] += data[i-1][j]

for i in range(N):
    s = ord(S[i])
    cnt += data[i][s-a]

print(cnt)
