import sys, collections
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
A_dict = collections.defaultdict(int)
cnt_all = N
cnt = 0

for a in A:
  A_dict[a] += 1

for item in A_dict.items():
  dupe_num = item[1]
  cnt_all -= dupe_num
  pair_cnt = cnt_all
  cnt += pair_cnt * dupe_num

print(cnt)