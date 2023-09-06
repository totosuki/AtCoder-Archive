O = list(input())
E = list(input())
rslt = ""
while True:
  if O:
    rslt += O.pop(0)
  if E:
    rslt += E.pop(0)
  if not O and not E:
    break
print(rslt)