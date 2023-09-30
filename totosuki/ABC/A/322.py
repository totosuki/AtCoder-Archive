# 38byte
# print(("_"+[*open(0)][1]).find("ABC"))

# 38byte
_,S=open(0)
print(("_"+S).find("ABC"))

# 41byte
# print(S.index("ABC")+1if"ABC"in S else-1)

# N = int(input())
# S = input()

# if "ABC" not in S:
#   print(-1)
#   exit()

# id = S.index("ABC")

# print(id + 1)