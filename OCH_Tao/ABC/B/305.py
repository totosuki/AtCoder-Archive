L = [0, 3, 4, 8, 9, 14, 23]
P, Q = map(lambda x: ord(x)-65, input().split())
print(L[max(P, Q)]-L[min(P, Q)])
