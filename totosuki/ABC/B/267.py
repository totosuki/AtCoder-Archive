from collections import defaultdict

S = input()
pin = [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]
pin_status = []
for i in range(len(pin)):
  tmp = [S[pin[i][j] - 1] for j in range(len(pin[i]))]
  pin_status.append(tmp)

#pin1が倒れているか判定
if pin_status[3][0] == "1":
  print("No")
  exit()

dict = defaultdict(int)
for i, p in enumerate(pin_status):
  if "1" in p:
    dict[i] = 1

bf_k = -1
now_k = -1

for k in dict.keys():
  if now_k == -1:
    now_k = k
    continue

  bf_k = now_k
  now_k = k
  if (now_k - bf_k) != 1:
    print("Yes")
    exit()
  else:
    continue

print("No")