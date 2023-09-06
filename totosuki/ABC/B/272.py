from itertools import combinations, permutations

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
members = list(range(1, N+1))
all_colabs = list(permutations(members, 2))
colabs = []
for i in range(len(data)):
  data[i][1:] = list(set(data[i][1:]))
  colab = list(combinations(data[i][1:], 2))
  colabs.append(colab)

#preprocessing all_colabs
all_colabs = [tuple(sorted(l)) for l in all_colabs]
all_colabs = list(set(all_colabs))

#preprocessing colab
colabs = [tuple(sorted(colabs[row][col])) for row in range(len(colabs)) for col in range(len(colabs[row]))]
colabs = list(set(colabs))

all_colabs.sort()
colabs.sort()

for d1, d2 in zip(all_colabs, colabs):
  if d1 != d2:
    print("No")
    break
else:
  print("Yes")