import sys; from sympy import factorint
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
rslt = 0
two = []
three = []
other = []

for i in range(N):
  data: dict =  factorint(A[i])

  two.append(0)
  three.append(0)
  other.append(-1)
  
  if data:
    sm = 0
    for key in data.keys():
      if key == 2:
        two[-1] = data[key]
      elif key == 3:
        three[-1] = data[key]
      else:
        sm += key ** data[key]
    other[-1] = sm

other_se = set(other)
if (len(other_se) == 1) or (len(other_se) == 2 and -1 in other_se):
  mn_two = min(two)
  mn_three = min(three)

  ans_two = sum(two) - (mn_two * N)
  ans_three = sum(three) - (mn_three * N)
  
  print(ans_two + ans_three)
else:
  print(-1)