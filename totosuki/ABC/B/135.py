N = int(input())
P = list(map(int, input().split()))
sort_P = sorted(P)
diff_cnt = 0

for p, s_p in zip(P, sort_P):
  if p != s_p:
    diff_cnt += 1

print("YES") if diff_cnt <= 2 else print("NO")