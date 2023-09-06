A, B = input().split()
a_sum = 0
b_sum = 0
for a, b in zip(A, B):
  a_sum += int(a)
  b_sum += int(b)
print(max([a_sum, b_sum]))