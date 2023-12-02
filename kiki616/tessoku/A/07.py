D = [0]*(int(input())+2)
N = int(input())
for i in range(N):
    L,R = map(int,input().split())
    D[L] += 1
    D[R+1] -= 1
for i in range(1,len(D)-1):
    D[i] += D[i-1]
    print(D[i])

# TLE Code order(N**2)
# D = [0 for _ in range(int(input())+1)]
# N = int(input())

# for i in range(N):
#     L,R = map(int,input().split())
#     D[L:R] += 1

# for i in D[1:]:
#     print(i)