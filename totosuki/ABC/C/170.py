# 109byte
X,N,*P=map(int,open(0).read().split())
print(min([n for n in range(105)if n not in P],key=lambda x:abs(X-x)))

# 114byte
# from numpy import*
# X,N,*P=map(int,open(0).read().split())
# print(min(setdiff1d(r_[0:105],P),key=lambda x:abs(X-x)))

# X, N = map(int, input().split())
# P = list(map(int, input().split()))
# answer = []
# for n in range(-5, 105):
#   if n not in P:
#     answer.append(n)
# print(min(answer, key = lambda n: abs(X - n)))

# X, N = map(int, input().split())
# P = list(map(int, input().split()))
# answer = 1 << 60

# for n in range(-5, 103):
#   if n in P: continue
#   if abs(X - n) < abs(X - answer):
#     answer = n

# print(answer)