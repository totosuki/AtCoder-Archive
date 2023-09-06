import sys
input = sys.stdin.buffer.readline

A, B = map(int, input().split())
answer = "No"

if B-1 == A:
  if B % 3 == 1:
    answer = "No"
  else:
    answer = "Yes"
    
print(answer)