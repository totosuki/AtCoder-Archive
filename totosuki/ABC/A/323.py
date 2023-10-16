S = input()
answer = "Yes"

for i in range(1, 16, 2):
  if S[i] == "1":
    answer = "No"

print(answer)

# Code Golf
# 38byte
print("YNeos"[input()[1::2]>"0"*8::2])
print("YNeos"["1"in input()[1::2]::2])