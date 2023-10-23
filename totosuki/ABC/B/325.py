# 99byte
a=[0]*24
for t in[*open(0)][1:]:
 w,x=map(int,t.split())
 for i in range(9):a[i-x]+=w
print(max(a))


# N = int(input())

# W = []
# X = []

# rslt = 0

# for _ in range(N):
#   w, x = map(int, input().split())
#   W.append(w)
#   X.append(x)

# for time in range(24):
#   member = 0
#   for i in range(N):
#     now = (X[i] + time) % 24
#     if 9 <= now <= 17:
#       member += W[i]
  
#   rslt = max(rslt, member)

# print(rslt)