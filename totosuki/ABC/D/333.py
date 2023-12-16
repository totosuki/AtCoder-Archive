# 152byte
# 150byte
from atcoder.dsu import*
N=int(input())-1
f=DSU(N+1)
exec("u,v=map(int,input().split());u>1and f.merge(u,v);"*N)
print(N-len(max(f.groups(),key=len)))

# 149byte
from atcoder.dsu import*;N,*A=open(0);N=int(N);D=DSU(N+1)
for a in A:u,v=map(int,a.split());u>1and D.merge(u,v)
print(N-len(max(D.groups(),key=len)))

# 151byte
# from atcoder.dsu import*
# (N,),*A=[map(int,l.split())for l in open(0)]
# f=DSU(N+1)
# for u,v in A:u>1and f.merge(u,v)
# print(N-len(max(f.groups(),key=len)))