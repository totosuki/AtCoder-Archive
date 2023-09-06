m = float(input())
if m < 100:
    print("00")
elif m >= 100 and m <= 5000:
    m = m/1000
    if m/1000 < 1:
        print(str(m).replace(".",""))
    else:
        print(int(m*10))
elif m >= 6000 and m <= 30000:
    print(int(m/1000 + 50))
elif m >= 35000 and m <= 70000:
    print(int(((m/1000 - 30) / 5 ) + 80))
elif m > 70000:
     print(89)
