def return_count(n):
  count = 0
  while True:
    if n % 2 == 1:
      return count
    n = n / 2
    count += 1

_ = int(input())
A = list(map(int, input().split()))
count = list(map(return_count, A))
print(min(count))