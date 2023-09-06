import string
alphabet = string.ascii_lowercase
S = input()
answer = "AC"
C_index = 2

if S[0] != "A":
  answer = "WA"

cnt = 0
for i in range(2, len(S)-1):
  if S[i] == "C":
    cnt += 1
    C_index = i
if cnt != 1:
  answer = "WA"

for i in range(len(S)):
  if i == 0 or i == C_index:
    if S[i] == "A" or S[i] == "C":
      continue
  if S[i] not in alphabet:
    answer = "WA"

print(answer)