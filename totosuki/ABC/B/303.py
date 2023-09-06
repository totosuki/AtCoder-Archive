N, M = map(int, input().split())
A = []
nakaii_list = []
hunaka_list = []
hunaka_count = 0
all_list = [[i, j]for i in range(1, N + 1) for j in range(1, N + 1) if i != j]

for i in range(M):
  A.append(list(map(int, input().split())))

for i, a in enumerate(A):
  for n in range(N - 1):
    nakaii_list.append([a[n], a[n + 1]])

nakaii_list = list(map(list, set(map(tuple, nakaii_list))))

for all_l in all_list:
  hunaka_count = 0
  for nakaii_l in nakaii_list:
    if all_l == nakaii_l or all_l == [nakaii_l[1], nakaii_l[0]]:
      continue
    else:
      hunaka_count += 1
  if hunaka_count >= len(nakaii_list):
    hunaka_list.append(all_l)

hunaka_count = 0
for li_1 in hunaka_list:
  for li_2 in hunaka_list:
    if li_1 == [li_2[1], li_2[0]]:
      hunaka_count += 0.5

print(int(hunaka_count))