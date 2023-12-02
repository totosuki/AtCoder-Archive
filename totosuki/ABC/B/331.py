N, S, M, L = map(int, input().split())

min_cost = float('inf')

for s_count in range((N // 6) + 2):
  for m_count in range((N // 8) + 2):
    for l_count in range((N // 12) + 2):
      total = 6 * s_count + 8 * m_count + 12 * l_count
      if total >= N:
        cost = S * s_count + M * m_count + L * l_count
        min_cost = min(min_cost, cost)

print(min_cost)
