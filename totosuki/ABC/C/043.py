N = int(input())
a = list(map(int, input().split()))
check_list = list(range(min(a),max(a) + 1))
cost_list = []
for check_num in check_list:
  cost = 0
  for n in a:
    cost += (check_num - n) ** 2
  cost_list.append(cost)
print(min(cost_list))