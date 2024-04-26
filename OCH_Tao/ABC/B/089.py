N = int(input())
S = list(input().split())
if len(list(set(S)))==3:
  print("Three")
else:
  print("Four")