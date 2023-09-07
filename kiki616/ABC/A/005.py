# [
#     print(
#         i[0] // i[1] 
#         for i in 
#         [list(map(int,input().split()))]
#     )
# ]

# print(input().split())

# x,y = map(int,input().split())
# print(y // x)

# a = list(map(int,input().split()))
# print(a[1] // a[0])

print(*[a[1] // a[0] for a in [list(map(int,input().split()))]])