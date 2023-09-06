SA = list(input())
SB = list(input())
SC = list(input())

turn = "a"
while True:
  if  turn == "a":
    if not SA:
      print("A")
      break
    else:
      turn = SA.pop(0)
  elif turn == "b":
    if not SB:
      print("B")
      break
    else:
      turn = SB.pop(0)
  elif turn == "c":
    if not SC:
      print("C")
      break
    else:
      turn = SC.pop(0)