# N, A, B = map(int, input().split())
# S = input()
# if B > 0:
#     print(S[A:-B])
# else:
#     print(S[A:])

# 52byte
A,S=open(0);N,A,B=map(int,A.split());print(S[A:N-B])

# 52byte
N,A,B=map(int,input().split())
print(input()[A:N-B])