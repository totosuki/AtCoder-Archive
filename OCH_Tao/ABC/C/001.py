Deg,Dis = map(int,input().split())
Dir = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
W1 = [0, 18, 96, 204, 330, 480, 648, 834, 1032, 1248, 1470, 1710]
W2 = [12, 90, 198, 324, 474, 642, 828, 1026, 1242, 1464, 1704, 1956]
for i in range(12):
  if W1[i]<=Dis<=W2[i]:
    print(f"{Dir[((Deg*10+1125)//2250)%16]} {i}" if i>0 else "C 0")
    break
else:
  print(f"{Dir[((Deg*10+1125)//2250)%16]} 12")
# 未AC
# from decimal import Decimal,ROUND_HALF_UP
# from math import floor
# deg,dis = map(float,input().split())
# dir = ["N","NNE","NNE","NE","NE","ENE","ENE","E","E","ESE","ESE","SE","SE","SSE","SSE","S","S","SSW","SSW","SW","SW","WSW","WSW","W","W","WNW","WNW","NW","NW","NNW","NNW","N"]
# W = [0.0,0.3,1.6,3.4,5.5,8.0,10.8,13.9,17.2,20.8,24.5,28.5,32.7]
# for i in range(12):
#   if W[i] <= Decimal(dis/60).quantize(Decimal("0.1"),ROUND_HALF_UP) < W[i+1]:
#     print(f"{dir[floor((deg)//112.5)]} {i}" if i>0 else f"C 0")

# Bパターン
# deg,dis = map(int,input().split())
# dir = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
# W = [0,18,96,204,330,480,648,834,1032,1248,1470,1710,1962]
# for i in range(12):
#   if W[i] <= dis < W[i+1]:
#     print(f"{dir[((deg*10+1125)//2250)%16]} {i}" if i>0 else "C 0")