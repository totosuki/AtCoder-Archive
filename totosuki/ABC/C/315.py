import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N = int(input())
diff_dict = defaultdict(list)
same_dict = defaultdict(list)

diff_list = []
same_list = []

for _ in range(N):
  F, S = map(int, input().split())
  diff_dict[F].append(S)
  same_dict[F].append(S)

for k in diff_dict.keys():
  tmp = diff_dict[k]
  tmp.sort(reverse = True)
  diff_list.append(tmp[0])

for k in same_dict.keys():
  tmp = same_dict[k]
  tmp.sort(reverse = True)
  if len(tmp) >= 2:
    same_list.append(tmp[0] + (tmp[1] // 2))

diff_list.sort(reverse = True)

same_rslt = max(same_list) if same_list else 0
diff_rslt = diff_list[0] + diff_list[1] if len(diff_list) >= 2 else 0

print(max(same_rslt, diff_rslt))