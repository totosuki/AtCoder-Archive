import sys, collections
input = sys.stdin.buffer.readline

N = int(input())
dict = collections.defaultdict(int)

for _ in range(N):
  S = input().decode().strip()

  if dict[S] == 0:
    print(S)
  else:
    print(f"{S}({dict[S]})")
  
  dict[S] += 1