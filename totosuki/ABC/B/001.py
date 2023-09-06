m = int(input())

if m < 100:
  print("00")
elif m <= 5000:
  vv = str(m//100).zfill(2)
  print(vv)
elif m <= 30000:
  vv = (m//1000) + 50
  print(vv)
elif m <= 70000:
  vv = ((m//1000) - 30) // 5 + 80
  print(vv)
elif m > 70000:
  print("89")