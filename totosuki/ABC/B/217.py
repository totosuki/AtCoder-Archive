S = {input() for _ in range(3)}

for contest in ("ABC", "ARC", "AGC", "AHC"):
  if not contest in S:
    print(contest)