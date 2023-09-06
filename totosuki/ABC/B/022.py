N = int(input())
l = set()
cnt = 0
for _ in range(N):
  flower = int(input())
  if flower in l:
    cnt += 1
  else:
    l.add(flower)
print(cnt)

# N = int(input())
# A = [int(input()) for _ in range(N)]
# cnt_l = [A.count(a) - 1 for a in set(A)]
# print(sum(cnt_l))

# N = int(input())
# A = []
# cnt = 0
# for i in range(N):
#   tmp = int(input())

#   if i == 0:
#     A.append(tmp)
#     continue
#   for j in range(i):
#     if A[j] == tmp:
#       cnt += 1
#       break
#   A.append(tmp)
# print(cnt)


# N = int(input())
# A = [int(input()) for _ in range(N)]
# status = [False for _ in range(N)]
# cnt = 0
# for i in range(N):
#   for j in range(i, N):
#     if i == j:
#       continue
    
#     if A[i] == A[j] and status[j] == False:
#       status[j] = True
#       cnt += 1

# print(cnt)