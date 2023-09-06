_ = input()
a, b = map(int, input().split())
_ = input()
P = list(map(int, input().split())) + [a,b]
if len(P) == len(set(P)):
  print("YES")
else:
  print("NO")

N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
l = P + [a,b]
if len(l) == len(set(l)):
  print("YES")
else:
  print("NO")