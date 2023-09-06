import sys
input = sys.stdin.buffer.readline

N = int(input())
aoki = 0
takahashi = 0
diff_l = list()
cnt = 0

for _ in range(N):
  A, B = map(int, input().split())
  aoki += A
  diff_l.append([A, A+B])

if aoki < takahashi:
  print(0)
  exit()

diff_l.sort(reverse=True)

for diff in diff_l:
  cnt += 1
  takahashi += diff[0]
  aoki -= diff[1]
  if aoki < takahashi:
    print(cnt)
    exit()