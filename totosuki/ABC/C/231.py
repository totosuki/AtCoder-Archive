# 117byte
# 121byte


from bisect import*
N,A,*X=map(str.split,open(0))
A=sorted(map(int,A))
for x in X:print(int(N[0])-bisect_left(A,int(*x)))

# 120byte
# from bisect import*
# N,A,*X=open(0)
# N,_=N.split()
# for x in X:print(int(N)-bisect_left(sorted(map(int,A.split())),iant(x)))

# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()

# for _ in range(Q):
#   X = int(input())
#   print(N - bisect_left(A, X))