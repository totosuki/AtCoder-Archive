N = int(input())
S0 = input()
S = list(S0.zfill(13))
S = "".join(sorted(S))
max_S = int("".join(sorted(list(S0), reverse = True)))

square_list = []
cnt = 0

for n in range(int(max_S ** 0.5)+1):
  square = str(n*n).zfill(13)
  square = sorted(list(square))
  square_list.append("".join(square))

for num in square_list:
  if S == num:
    cnt += 1

print(cnt)