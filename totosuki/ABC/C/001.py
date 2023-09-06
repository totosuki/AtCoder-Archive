import sys
input = sys.stdin.buffer.readline

def my_round(N, power: int):
  adjust = 1 if N >=0 else -1
  shift = 10 ** (power-1)
  N = abs(N * shift)
  return (int(N + 0.5) / shift) * adjust

deg, dis = map(int, input().split())
deg = deg / 10
dis = my_round(dis/60, 2)
rslt_deg = ""
rslt_dis = 0

# 風向
if 348.75 <= deg or deg < 11.25: rslt_deg = "N"
elif deg < 33.75: rslt_deg = "NNE"
elif deg < 56.25: rslt_deg = "NE"
elif deg < 78.75: rslt_deg = "ENE"
elif deg < 101.25: rslt_deg = "E"
elif deg < 123.75: rslt_deg = "ESE"
elif deg < 146.25: rslt_deg = "SE"
elif deg < 168.75: rslt_deg = "SSE"
elif deg < 191.25: rslt_deg = "S"
elif deg < 213.75: rslt_deg = "SSW"
elif deg < 236.25: rslt_deg = "SW"
elif deg < 258.75: rslt_deg = "WSW"
elif deg < 281.25: rslt_deg = "W"
elif deg < 303.75: rslt_deg = "WNW"
elif deg < 326.25: rslt_deg = "NW"
elif deg < 348.75: rslt_deg = "NNW"
# 風力
if dis <= 0.2: rslt_dis, rslt_deg = 0, "C"
elif dis <= 1.5: rslt_dis = 1
elif dis <= 3.3: rslt_dis = 2
elif dis <= 5.4: rslt_dis = 3
elif dis <= 7.9: rslt_dis = 4
elif dis <= 10.7: rslt_dis = 5
elif dis <= 13.8: rslt_dis = 6
elif dis <= 17.1: rslt_dis = 7
elif dis <= 20.7: rslt_dis = 8
elif dis <= 24.4: rslt_dis = 9
elif dis <= 28.4: rslt_dis = 10
elif dis <= 32.6: rslt_dis = 11
else: rslt_dis = 12

print(rslt_deg, rslt_dis)