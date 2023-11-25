# 57byte
# 68byte
# 71byte
# 71byte
L,A=open(0)
_,L=int(L.split())
print(sum(int(a)>=L for a in A.split()))

# 66byte
_,L,*A=map(int,open(0).read().split())
print(sum(a>=L for a in A))

# 70byte
# _,L=input().split()
# print(sum(a>=L for a in map(int,input().split())))

# 74byte
# from numpy import*
# _,L,*A=map(int,open(0).read().split())
# print(sum(A>=L))



# N, L = map(int, input().split())
# A = list(map(int, input().split()))
# cnt = 0

# for a in A:
#   if a >= L:
#     cnt += 1
# print(cnt)