N = int(input())
d_list = []
for _ in range(N):
  d_list.append(int(input()))
d_set = set(d_list)
print(len(d_set))