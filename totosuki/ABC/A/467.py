from fractions import Fraction

H, W = map(int, input().split())
H *= 0.01
BMI = float(Fraction(W) / Fraction(H) / Fraction(H))

if BMI >= 24.999:
    print("Yes")
else:
    print("No")