S = input()
S0 = S[0].upper()
S1 = list(map(lambda s: s.lower(), S[1:]))
print(S0 + "".join(S1))