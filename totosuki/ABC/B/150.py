N = int(input())
S = input()
cnt = 0

for i in range(N-2):
  if S[i]+S[i+1]+S[i+2] == "ABC":
    cnt += 1

print(cnt)