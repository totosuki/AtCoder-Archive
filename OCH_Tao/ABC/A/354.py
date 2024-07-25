H = int(input())
cnt = 0
i = 0
while True:
  cnt+=2**i
  i+=1
  if H<cnt:
    print(i)
    break