# 85byte
A=[]
for s in[*open(0)][1:]:a,b=map(int,s.split());A.append(b)if a<2else print(A[-b])

# 102byte
A=[]
for _ in[0]*int(input()):
  a,b=map(int,input().split())
  if a<2:A.append(b)
  else:print(A[-b])

# Q = int(input())
# A = []

# for _ in range(Q):
#   a, b = map(int, input().split())
#   if a == 1:
#     A.append(b)
#   else:
#     print(A[-b])