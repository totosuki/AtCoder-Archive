N, Q = map(int, input().split())
A = list(map(int, input().split()))

dict_A = {i:A[i] for i in range(N)}
sorted_A = sorted([(A[i], i) for i in range(N)])
six = [sorted_A[i][0] for i in range(6)]

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    B = [dict_A[b-1] for b in B]
    
    six_copy = six.copy()
    
    for i in range(len(B)):
        if B[i] in six_copy:
            six_copy.remove(B[i])
    
    print(six_copy[0])
