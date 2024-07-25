SX,SY = map(int,input().split())
TX,TY = map(int,input().split())
cnt = 0
cnt+=abs(SY-TY)
if abs(SX-TX)<=cnt:
  print(cnt)
else:
  print(cnt+(abs(SX-TX)-cnt)//2)