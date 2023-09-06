N = input()
answer = "No"

for i in range(10):
  kaibun_N = "".join(reversed(list(N)))
  if N == kaibun_N:
    answer = "Yes"
  
  N = "0" + N

print(answer)