N = int(input())
answer = "No"
S = input()

if N % 2:
  answer = "No"
else:
  if S[:N//2] == S[N//2:]:
    answer = "Yes"

print(answer)