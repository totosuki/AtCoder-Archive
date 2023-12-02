T = int(input())
N = int(input())
li = [0] * (T+3)

# index 1 = 0時
for i in range(N):
    L,R = map(int,input().split())
    li[L+1] += 1
    li[R+1] -= 1

for i in range(1,len(li)-2):
    li[i] = li[i-1] + li[i]
    print(li[i])

# 10
# 7
# 0 3
# 2 4
# 1 3
# 0 3
# 5 6
# 5 6
# 5 6