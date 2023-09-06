import sys
input = sys.stdin.buffer.readline

S = input().decode().strip()
T = input().decode().strip()
answer = "No"
diff_cnt = 0

for s, t in zip(S, T):
  if s != t:
    diff_cnt += 1

if diff_cnt == 0:
  answer = "Yes"

if diff_cnt == 2:
  for i in range(len(S)-1):
    if S[i]+S[i+1] == T[i+1]+T[i]:
      answer = "Yes"

print(answer)