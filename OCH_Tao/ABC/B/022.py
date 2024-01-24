# 愚直コード(CPythonではTLE、PyPyで約1600ms)
# N = int(input())
# l = []
# cnt = 0
# for i in range(N):
#   a = int(input())
#   if a not in l:
#     l.append(a)
#   else:
#     cnt += 1
# print(cnt)

N = int(input())
a = []
for i in range(N):
  a.append(int(input()))
l = list(set(a))
print(len(a)-len(l))