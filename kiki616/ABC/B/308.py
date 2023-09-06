N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))

値段表 = {"No":P[0]}
お会計 = 0
del P[0]

for i in range(M):
    値段表.update({D[i]:P[i]})

for i in C:
    if i in 値段表:
        お会計 = お会計 + 値段表[i]
    else:
        お会計 = お会計 + 値段表["No"]

print(お会計)