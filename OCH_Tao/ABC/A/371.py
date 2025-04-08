AB,AC,BC = input().split()
if AB==AC:
  if AB==">":
    print("B" if BC==">" else "C")
  else:
    print("C" if BC==">" else "B")
elif AC==BC:
  if AC==">":
    print("B" if AB==">" else "A")
  else:
    print("A" if AB==">" else "B")
else:
  if AB==">":
    print("C" if AC==">" else "A")
  else:
    print("A" if AC==">" else "C")