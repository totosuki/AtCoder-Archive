N = int(input())
C = []
A = []
luck = []
isis = True
for i in range(N):
    C.append(int(input()))
    A.append(list(map(int,input().split())))
X = int(input())

for i in range(N):
    if X in A[i]:
        luck.append(A[i])

for i in reversed(range(36)):
    ans = []
    for l in luck:
        if i == len(l):
            ans.append(A.index(l)+1)
    if ans:
        isis = False
        print(*ans)

if isis:
    print(0)

# import random
# N = random.randint(1,100)
# print(N)
# for i in range(N):
#     C = random.randint(1,37)
#     A = []
#     for l in range(C):
#         li = [i for i in range(0,36)]
#         a = random.choice(li)
#         li.remove(a)
#         A.append(a)
#     print(C)
#     print(*A)
# print(random.randint(0,36))