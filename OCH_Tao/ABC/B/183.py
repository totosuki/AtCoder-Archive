SX,SY,GX,GY = map(int,input().split())
print(SX+(SY/(SY+GY))*(GX-SX))