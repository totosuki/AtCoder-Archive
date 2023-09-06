import sys
input = sys.stdin.buffer.readline

A, B, C = map(int, input().split())

if C % 2 == 0:
  A, B = map(abs, (A, B))
  if A > B: print(">")
  elif A < B: print("<")
  else: print("=")
elif C % 2 == 1:
  if A > B: print(">")
  elif A < B: print("<")
  else: print("=")