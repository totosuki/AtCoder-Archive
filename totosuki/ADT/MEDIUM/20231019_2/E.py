N = int(input())
A = list(map(int, input().split()))
A.sort(reverse = True)

odd = [a for a in A if a % 2 == 0]
even = [a for a in A if a % 2 == 1]
odd_mxes = odd[:2]
even_mxes = even[:2]

if len(odd_mxes) < 2 and len(even_mxes) < 2:
  print(-1)
else:
  rslt = max(sum(odd_mxes), sum(even_mxes))
  print(rslt)