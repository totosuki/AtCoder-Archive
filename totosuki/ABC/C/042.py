N, K = map(int, input().split())
D = list(map(int, input().split()))

# no_D = []
# result = ""

# for t in [0,1,2,3,4,5,6,7,8,9]:
#   flag = False
#   for d in D:
#     if t != d:
#       continue
#     else:
#       flag = True
#   if not flag:
#     no_D.append(t)

while True:
  flag = False
  for n in str(N):
    if int(n) in D:
      flag = True
  
  if flag:
    N += 1
    continue
  else:
    break

print(N)

# str_n = str(N)
# str_10n = "0" + str(N)

# for n in str_n:
#   n = int(n)
#   for i in no_D:
#     if i >= n:
#       result += str(i)
#       break

# if result[1:] >= str_n:
#   result = result[1:]

# if result[0] == "0":
#   result[0] = str(no_D[1])

# print(result)