import sys
input = sys.stdin.buffer.readline

S = input().decode().strip()
cnt = 0
answer = "Yes"

if "xxx" in S:
  answer = "No"

if "oo" in S:
  answer = "No"

if "oxo" in S:
  answer = "No"

print(answer)