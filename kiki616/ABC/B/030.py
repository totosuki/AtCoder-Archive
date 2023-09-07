n,m = map(int,input().split())
short = int(360 / 12) #30
long  = int(360 / 30) #6
answer = 0
if n >= 12:
    n = n - 12

if n*short < m*long:
    answer = m*long - n*short
else:
    answer = n*short - m*long

if answer > 180:
    print(360 - answer)
else:
    print(answer)