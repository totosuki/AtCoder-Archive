N, A, B = map(int, input().split())
rslt = (N // (A + B)) * A
amari = N % (A + B)

if amari >= A:
  rslt += A
else:
  rslt += amari

print(rslt)