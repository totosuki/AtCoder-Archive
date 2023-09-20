import sys
input = sys.stdin.buffer.readline

N = int(input())
H = [0] + list(map(int, input().split()))

d = [0] * (N+1)
d[2] = a(H[1] - H[2])

for i in range(3, N+1):
  d[i] = min(a(H[i-1] - H[i]) + d[i-1], a(H[i-2] - H[i]) + d[i-2])

p = N
r = []

while True:
  r.append(p)
  
  if p == 1:
    break
  
  if (d[p-1] + a(H[p-1] - H[p])) == d[p]:
    p -= 1
  else:
    p -= 2

r.reverse()
print(len(r))
print(*r)

# Code Golf
# N=int(input())
# a=abs
# H=[0]+list(map(int,input().split()))
# d=[0]*(N+1)
# d[2]=a(H[1]-H[2])
# for i in range(3,N+1):d[i]=min(a(H[i-1]-H[i])+d[i-1],a(H[i-2]-H[i])+d[i-2])
# p=N
# r=[]
# while 1:
#   r.append(p)
#   if p<2:break
#   p-=1 if d[p-1]+a(H[p-1]-H[p])==d[p]else 2
# print(len(r))
# print(*reversed(r))