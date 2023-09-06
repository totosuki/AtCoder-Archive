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
  diff_l.append([A,B])

diff_l.sort(reverse=True, key = lambda x: 2*x[0]+x[1])

for diff in diff_l:
  cnt += 1
  takahashi += diff[0] + diff[1]
  aoki -= diff[0]
  if aoki < takahashi:
    print(cnt)
    exit()