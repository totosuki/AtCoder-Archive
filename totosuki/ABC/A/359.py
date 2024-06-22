# 32byte
print(open(0).read().count("s"))

# 58byte
print("".join(input()for _ in[0]*int(input())).count("s"))

# N = int(input())
# cnt = 0

# for i in range(N):
#   S = input()
#   if S == "Takahashi":
#     cnt += 1

# print(cnt)