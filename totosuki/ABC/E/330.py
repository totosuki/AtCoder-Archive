from collections import defaultdict

def return_A_cnt(N, A:list):
  A_cnt = defaultdict(int)
  for a in A:
    A_cnt[a] += 1
  return A_cnt

def return_first_mex(N, A_sorted:list, A_cnt:dict):
  A0 = A_sorted[0]
  mex = {"under":[A0, A_cnt[A0]]} # {under: [右端,右端の個数], "upper": [左端,左端の個数]}
  for i in range(1, N):
    if A_sorted[i] - A_sorted[i-1] > 1:
      mex["upper"] = [A_sorted[i-1], A_cnt[A_sorted[i-1]]]
      break
  if "upper" not in mex:
    mex["upper"] = [A_sorted[-1], A_cnt[A_sorted[-1]]]
  return mex

def solve(N, Q, A: list, A_cnt: dict, A_sorted:list, mex: dict):
  for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1

def main():
  N, Q = map(int, input().split())
  A = list(map(int, input().split()))
  A_cnt = return_A_cnt(N, A)
  A_sorted = sorted(A)
  mex = return_first_mex(N, A_sorted, A_cnt)
  print(mex)
  solve(N, Q, A, A_cnt, A_sorted, mex)

main()


# 毎回Aに含まれない最小の非負整数を出力する

# [0, 1, 2, 3, 6, 7, 9, 10, 11, 16]を[(0,3),(6,7),(9,11),(16,16)]で管理する