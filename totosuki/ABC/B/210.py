# 52byte
_,S=open(0)
print(S.find("1")%2*"Aoki"or"Takahashi")
print(S.find("1")%2*"Yes"or"No")
print("NYoe s"[S.find("1")%2::2])

# 54byte
# print(["Takahashi","Aoki"][[*open(0)][1].find("1")%2])

# print("TAaokkaih a s h i"[S.find("1")%2::2])

# import sys
# input = sys.stdin.buffer.readline

# N = int(input())
# S = input().decode().strip()

# for i in range(N):
#   if S[i] == "1":
#     print("Takahashi") if i % 2 == 0 else print("Aoki")
#     break