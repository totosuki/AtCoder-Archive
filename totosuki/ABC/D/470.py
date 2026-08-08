N, Q = map(int, input().split())
P = list(map(int, input().split()))

d1 = {} # 値が何番目か（switch == False）
d2 = {} # 何番目に何の値か（switch == False）

switch = False

for i in range(N):
    d1[P[i]] = i+1
    d2[i+1] = P[i]

for _ in range(Q):
    q, *xy = map(int, input().split())

    if q == 1:
        x, y = xy
        if switch == False:
            xp = d2[x]
            yp = d2[y]
            d1[xp] = y
            d1[yp] = x
            d2[y] = xp
            d2[x] = yp
        else:
            xp = d1[x]
            yp = d1[y]
            d2[xp] = y
            d2[yp] = x
            d1[y] = xp
            d1[x] = yp
    else:
        switch = not switch

for i in range(1, N+1):
    if switch == False:
        print(d2[i], end=" ")
    else:
        print(d1[i], end=" ")

# 値が何番目にあるかと、何番目に何の値があるかを管理すればいけそう
# Key, Value も Swap しそう
# 二次元の List で管理してみる -> Index アクセスができないので、二つの辞書にする
