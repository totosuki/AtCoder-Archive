def return_row_cnt(N, S):
  row_cnt = [0] * N
  for i in range(N):
    for j in range(N):
      if S[i][j] == 'o':
        row_cnt[i] += 1
  return row_cnt

def return_col_cnt(N, S):
  col_cnt = [0] * N
  for i in range(N):
    for j in range(N):
      if S[j][i] == 'o':
        col_cnt[i] += 1
  return col_cnt

def solve(N, S, row_cnt, col_cnt):
  rslt = 0
  for i in range(N):
    for j in range(N):
      if S[i][j] == "x": continue
      row_rslt = row_cnt[i] - 1 # 何通りか
      col_rslt = col_cnt[j] - 1 # 何通りか
      if row_rslt > 0 and col_rslt > 0:
        rslt += row_rslt * col_rslt
  return rslt

def main():
  N = int(input())
  S = [list(input()) for _ in range(N)]

  row_cnt = return_row_cnt(N, S) # row_cnt[i]: i行目にoが何個あるか
  col_cnt = return_col_cnt(N, S) # col_cnt[i]: i列目にoが何個あるか
  
  rslt = solve(N, S, row_cnt, col_cnt)
  
  print(rslt)

main()


# Input
# 3
# ooo
# oxx
# xxo
# output
# 4

# (1,1),(1,2),(2,1)
# (1,1),(1,3),(2,1)
# (1,1),(1,3),(3,3)
# (1,2),(1,3),(3,3)

# 条件
# ・組に含まれる3ますは、すべて異なる
# ・組に含まれるマスはすべてoである
# ・マスのうち、丁度２つが同じ行にある
# ・マスのうち、丁度２つが同じ列にある