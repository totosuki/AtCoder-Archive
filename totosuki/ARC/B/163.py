N, M = map(int, input().split())
A = list(map(int, input().split()))
A1 = A[0]
A2 = A[1]
up_L = []
dn_L = []
cnt = 0
rslt = []

for i in range(2, N):
  if A[i] < A1:
    # dn_L.append(A1 - A[i])
    dn_L.append(A[i])
  elif A[i] > A2:
    # up_L.append(A[i] - A2)
    up_L.append(A[i])
  else:
    cnt += 1
  # 既に満たされてる場合はここで0出力する
  if cnt == M:
    print(0)
    exit()

up_L.sort()
dn_L.sort()
up_len = len(up_L)
dn_len = len(dn_L)
nokori = M - cnt

print(f"up_L: {up_L}")
print(f"dn_L: {dn_L}")
print(f"up_len: {up_len}")
print(f"dn_len: {dn_len}")
print(f"cnt: {cnt}")

up_cum = [A2] + up_L
dn_cum = [A1] + dn_L


# 累積和?を考える
for i in reversed(range(1, up_len+1)):
  up_cum[i] = up_L[i-1] - up_cum[i-1]
for i in reversed(range(1, dn_len+1)):
  dn_cum[i] = dn_cum[i-1] - dn_L[i-1]
for i in range(2, up_len+1):
  up_cum[i] = up_cum[i-1] + up_cum[i]
for i in range(2, dn_len+1):
  dn_cum[i] = dn_cum[i-1] + dn_cum[i]

print(f"up_cum: {up_cum}")
print(f"dn_cum: {dn_cum}")

for i in range(M - cnt + 1):
  # 空配列処理
  if up_len == 0:
    rslt.append(dn_cum[M-cnt])
    continue
  if dn_len == 0:
    rslt.append(up_cum[M-cnt])
    continue

  # RE避け
  if nokori - i > dn_len or i > up_len:
    continue

  # dn_Lのみの場合
  if i == 0:
    rslt.append(dn_cum[nokori])
    continue
  
  # print(f"i: {i}")
  rslt.append(up_cum[i] + dn_cum[nokori-i])

print(min(rslt))

# for i in range(M - cnt + 1):
#   # 空配列処理
#   if up_len == 0:
#     rslt.append(dn_L[(M-cnt)-1])
#     continue
#   if dn_len == 0:
#     rslt.append(up_L[(M-cnt)-1])
#     continue

#   # RE避け
#   if nokori - i > dn_len or i > up_len:
#     continue

#   # dn_Lのみの場合
#   if i == 0:
#     rslt.append(dn_L[nokori - 1])
#     continue
  
#   rslt.append(up_L[i - 1] + dn_L[(nokori - i) - 1])

# print(min(rslt))

# A[0]もA[1]も動かすことができる
# up_Lでi回目までやって、dn_Lを残りやる 計算量心配
# 別解
# sortしたときに一個前との差分を考える
# 累積和で考える