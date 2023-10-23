# 127byte
# 99byte
from sympy import*
print(min([0if a%2else factorint(a)[2]for a in map(int,[*open(0)][1].split())]))

# 103byte
# 101byte
# N,A=open(0)
# C={99}
# for a in map(int,A.split()):
#  c=0
#  while a%2<1:c,a=c+1,a//2
#  C.add(c)
# print(min(C))


# N,A=open(0)
# A=list(map(int,A.split()))
# c=0
# while 1:
#  for i in range(int(N)):
#   if A[i]%2:break
#   else:A[i]//=2
#  else:
#   c+=1
#   continue
#  break
# print(c)

# n=int(input())
# a=list(map(int,input().split()))
# i=0
# f=True
# while f:
#  num = 1
#  for x in a:
#   if x%2:
#    f=False
#    break
#   else:a[num-1]=x//2
#   num += 1
#   if num==n:i+=1

# print(i)