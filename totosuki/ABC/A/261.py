L1, R1, L2, R2 = map(int, input().split())
min_r = min(R1, R2)
max_l = max(L1, L2)

if min_r - max_l > 0:
  print(min_r - max_l)
else:
  print(0)

# l1 = list(range(L1, R1))
# l2 = list(range(L2, R2))
# if R1 <= L2:
#   print(0)
# elif R1 > L2 and L1 < L2:
#   if R1 <= R2:
#     print(R1 - L2)
#   else:
#     print(R2 - L2)
# elif R1 > R2 and L1 < R2:
#   if L1 >= L2:
#     print(R2 - L1)
#   else:
#     print(R2 - L2)
# elif L1 >= R2:
#   print(0)


# if R1 > L2:
#   if L1 > L2:
#     print(R1 - L1)
#   else:
#     print(R1 - L2)
# else:
#   print(0)