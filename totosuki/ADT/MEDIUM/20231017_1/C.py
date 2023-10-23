# 30byte
print(*sorted(input()),sep="")

S = list(input())
S.sort()
print("".join(S))