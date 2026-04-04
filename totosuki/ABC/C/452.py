N = int(input())
A = []
B = []
base = ord("a")

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b-1)

M = int(input())
S = []
ok = [[False]*26 for _ in range(N)]

for i in range(M):
    s = input()
    S.append(s)
    
    for j in range(N):
        if len(s) != A[j]: continue
        ok[j][ord(s[B[j]]) - base] = True

for s in S:
    if len(s) != N:
        print("No")
        continue

    flag = True

    for i in range(N):
        if not ok[i][ord(s[i]) - base]:
            flag = False
    
    print("Yes" if flag else "No")

# N列目に何の文字が置けるかどうかのリスト