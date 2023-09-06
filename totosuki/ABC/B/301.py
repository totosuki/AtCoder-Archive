import sys
sys.setrecursionlimit(10000)

N = int(input())
A = list(map(int, input().split()))

def alignment_numbers(A, continue_num = 0, old_n = None, change_count = 0):
  for i, n in enumerate(A[continue_num:]):
    i += continue_num

    if change_count >= N:
      break

    if old_n == None:
      old_n = n
      change_count += 1
      continue

    diff = n - old_n

    if abs(diff) <= 1:
      old_n = n
      change_count += 1
      continue
    else:
      if diff > 1:
        A.insert(i, old_n + 1)
        old_n += 1
      else:
        A.insert(i, old_n - 1)
        old_n -= 1
      continue_num = i + 1
      return alignment_numbers(A, continue_num, old_n, change_count)
  return A

A = alignment_numbers(A)
print("".join(map(lambda x: f"{x} ", A)))