import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

idict = {p : i for i, p in enumerate(P)}
ans = []
seen = [[False] * N for _ in range(N)]
now = [1, N]
q = []


while True:
  diff, Pl = now
  Pr = Pl - diff
  
  if now[0] >= N:
    break
  
  if Pr < 0:
    now = [diff + 1, N]
    continue
  
  Plid = idict[Pl]
  
  if Plid + K >= N:
    now = [diff, Pl - 1]
    continue
  
  
  for Prid in range(Plid + K, N):
    if P[Prid] == Pr and not seen[Plid][Prid]:
      ans.append((Plid+1, Prid + 1))
      seen[Plid][Prid] = True
      idict[Pl] = Prid
      idict[Pr] = Plid
      heapq.heappush(q, (1, Pr))
      heapq.heappush(q, (1, Pl))
      while q:
        diff, sPl = heapq.heappop(q)
        sPr = sPl - diff
        
        
        if [diff, sPl] >= now:
          q = []
          break
        
        if sPr < 0:
          continue
        
        sPlid = idict[sPl]
        
        if sPlid + K >= N:
          continue
        
        for sPrid in range(sPlid + K, N):
          if P[sPrid] == sPr and not seen[sPlid][sPrid]:
            ans.append((sPlid+1, sPrid+1))
            seen[sPlid][sPrid] = True
            idict[sPl] = sPrid
            idict[sPr] = sPlid
            heapq.heappush(q, (1, sPl))
            heapq.heappush(q, (1, sPr))
            break
        else:
          heapq.heappush(q, (diff + 1, sPr))
          heapq.heappush(q, (diff + 1, sPl))
      break
  
  now = [diff, Pl - 1]

print(len(ans))
for a in ans:
  print(*a)

# 最大 124750 通りっぽい

# 基本としてPlとPrの差が小さいものから交換していく
# Plを見たときに、Kこ右隣りから末端までにPl-(現在の差の最小値)のPrが存在するか確認する
# 存在した場合スワップするが、seen[Pl][Pr]がしてたらスキップ
# スワップしたあとに、その２つの値に対して以下のことをする
# ・スワップした値をヒープキューに入れる
# ・ヒープキューの構造は[(1から現在の差の最小値のどれか, スワップした値)]
# ・ヒープキューからデータを一つ取り出す
#   具体的には、スワップしたあとのPl-1が、Kこ右隣りから末端までに存在するか確認する
# ・存在したらseen[Pl][Pr]が大丈夫か確認してスワップ
# ・スワップしたら、1にリセットしてヒープキューに追加する（最初に戻る）