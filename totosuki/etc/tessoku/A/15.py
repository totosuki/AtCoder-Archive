# 104byte
# 108byte
import bisect as f
_,A=open(0)
A=list(map(int,A.split()))
B=sorted(set(A))
print(*[f.bisect(B,a)for a in A])

# 106byte
# import bisect as f
# input()
# A=list(map(int,input().split()))
# print(*[f.bisect(sorted(set(A)),a)for a in A])

# 107byte
# import bisect as f
# _,A=list(map(int,open(0).read().split()))
# print(*[f.bisect(sorted(set(A)),a)for a in A])