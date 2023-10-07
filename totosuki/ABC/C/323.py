from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]
scores = defaultdict(list)
max_point = 0

new_A = [0] * M

# index付きAを作成
for i in range(M):
  new_A[i] = [A[i], i+1]


# 各キャラのどのindexの問題を解いているか
for i in range(N):
  point = i+1
  
  for j in range(M):
    if S[i][j] == "o":
      point += A[j]
      scores[i+1].append(new_A[j][1])
  
  max_point = max(max_point, point)

new_A.sort(key = lambda x: -x[0])

for i in range(N):
  cnt = 0
  score = i+1
  for j in range(len(scores[i+1])):
    score += A[scores[i+1][j]-1]
  
  if score == max_point:
    print(cnt)
    continue
  
  for j in range(M):
    if new_A[j][1] not in scores[i+1]:
      score += new_A[j][0]
      cnt += 1
      if score >= max_point:
        print(cnt)
        break

# A.sort(reverse=True)

# 解いていない問題の中で多い方から何問で一番高いスコアになるか