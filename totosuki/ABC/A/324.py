# 57byte
print("NYoe s"[eval([*open(0)][1].replace(*" ="))::2])

# 50byte
print("YNeos"[len({*[*open(0)][1].split()})>1::2])

# 51byte
# _,A=open(0)
# print("YNeos"[len({*open(0)[1:].split()})!=1::2])

# 53byte
# _,A=open(0)
# print("YNeos"[len(set(A.split()))!=1::2])

# N = int(input())
# A = set(list(map(int, input().split())))

# if len(A) == 1:
#   print("Yes")
# else:
#   print("No")