A,B,K = map(int,input().split())
l = []
l.extend(list(range(A,A+K)))
l.extend(list(range(B,B-K,-1)))
l = list(set(l))
l = [i for i in l if A<=i<=B]
l.sort()
print("\n".join([str(i) for i in l]))