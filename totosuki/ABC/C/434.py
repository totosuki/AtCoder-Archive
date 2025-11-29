test_cnt = int(input())

for _ in range(test_cnt):
    N, H = map(int, input().split())
    T = [0]
    L = [0]
    U = [0]
    can = [[H, H]] # Ti時のタイミングで可能な、(High, Low)

    flag = True

    for _ in range(N):
        t, l, u = map(int, input().split())
        T.append(t)
        L.append(l)
        U.append(u)
    
    for i in range(1, N+1):
        high = can[i-1][0]
        low = can[i-1][1]
        dist = T[i] - T[i-1]
        can.append([-1, -1])

        if high + dist >= U[i]:
            can[i][0] = U[i]
        else:
            can[i][0] = high + dist
        
        if low - dist <= L[i]:
            can[i][1] = L[i]
        else:
            can[i][1] = low - dist
        
        # 到達可能かどうか
        if can[i][0] < L[i] or can[i][1] > U[i]:
            # print(f"T[i]: {T[i]}\ncan: {can}")
            flag = False
            break
    
    print("Yes" if flag else "No")
