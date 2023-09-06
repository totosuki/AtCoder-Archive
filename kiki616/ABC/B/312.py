N,M = map(int,input().split())
S = []
cnt = []
for i in range(N):
    S.append(input())

for i in range(N-8):
    for l in range(M-8):
        judge = True
        for k in range(4):
            for j in range(4):
                
                if k==3 or j == 3:
                    if S[i+k][l+j] != '.':
                        judge = False
                else:
                    if S[i+k][l+j] != '#':
                        judge = False

        for k in range(4):
            for j in range(4):

                if k==3 or j == 3:
                    if S[(i+8)-k][(l+8)-j] != '.':
                        judge = False
                else:
                    if S[(i+8)-k][(l+8)-j] != '#':
                        judge = False

        if judge:
            cnt.append([i+1,l+1])

for i in cnt:
    print(*i)