N,M = map(int,input().split())
p = []
seek = False
for i in range(N):
    p.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if p[i][0] >= p[j][0]:
            isis = True
            for l in p[i][2:]:
                if not l in p[j][2:]:
                    isis = False
            if isis:
                if (p[i][0] > p[j][0]) or (len(p[i][2:]) < len(p[j][2:])):
                    seek = True
if seek:
    print("Yes")
else:
    print("No")