N = int(input())
cards = []
for i in range(N):
  a, c = map(int, input().split())
  cards.append((a, c, i))

cards.sort(key=lambda x: (-x[0], x[1], x[2]))
remaining_cards = []

min_cost = float('inf')

for strength, cost, id in cards:
  if cost < min_cost:
    remaining_cards.append((strength, cost, id))
    min_cost = cost

ans = []
for strength, cost, id in remaining_cards:
  ans.append(id + 1)

print(len(ans))
print(*sorted(ans))