N = int(input())
S = list(input())
Q = int(input())

S1 = S[:N]
S2 = S[N:]

flag = False

for _ in range(Q):
    T, A, B = map(int, input().split())
    
    if T == 1:
        A, B = map(lambda x: x-1, [A, B])
        if A >= N: # Aが半分より大きかったら
            S2[A-N], S2[B-N] = S2[B-N], S2[A-N]
        elif B < N: # Bが半分より小さかったら
            S1[A], S1[B] = S1[B], S1[A]
        else: # それ以外（Aが半分より小さくて、Bが半分より大きい）
            S1[A], S2[B-N] = S2[B-N], S1[A]
    if T == 2:
        S1, S2 = S2, S1

print("".join(S1 + S2))