

# N,K = map(int, input().split())
# a = []
# b = []
# for i in range(N):
#     a_,b_ = map(int, input().split())
#     a.append(a_)
#     b.append(a_)

# is_run = True
# count = 0
# while is_run:
#     if sum(b) >= K:
#         is_run = True
#         print(count)
#     count = count+min(a)
#     a = list(map(lambda a:a - min(a)))
#     a.count(0)
#     a.pop(a.index(min(a)))

'''
N = int(input())
A = []
B = []
for i in range(N):
    A.append(input())

# # AのコピーをBに作る
# B = A.copy()

# 0行目とN行目を右へ一つずらす。
for i in range(N):
    if i == N :
        B.append(A[0][0])
    else:
        B.append(A[0][N+1])
B.append()
# Aのコピーから0列目のindexをマイナス1するこの時に0の場合はNにする。
# AのコピーからN列目のindexをプラス1するこの時に0の場合はNにする。
'''
