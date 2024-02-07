V,A,B,C = map(int,input().split())
for i in range(100000):
  V-=A
  if V<0:
    print("F")
    break
  V-=B
  if V<0:
    print("M")
    break
  V-=C
  if V<0:
    print("T")
    break