T = int(input())
N = []
tests = []
for _ in range(T):
  N.append(int(input()))
  tests.append(list(map(int, input().split())))

for test in tests:
  print(len([t for t in test if t % 2]))