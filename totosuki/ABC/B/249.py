import sys
input = sys.stdin.buffer.readline

S = input().decode().strip()
answer = "Yes"

for s in S:
  if s.islower():
    break
else:
  answer = "No"

for s in S:
  if s.isupper():
    break
else:
  answer = "No"

if len(S) != len(set(S)):
  answer = "No"

print(answer)