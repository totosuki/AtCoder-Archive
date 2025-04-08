print(int("".join(input().split())[::-1], base=2))

# A = list(map(lambda x: bool(int(x)), input().split()))
# cnt = 0
# for i in range(64):
#   if A[i]:
#     cnt += 2**i
# print(cnt)

# A = list(map(int, input().split()))
# print(sum([2**i*j for i, j in enumerate(A)]))
