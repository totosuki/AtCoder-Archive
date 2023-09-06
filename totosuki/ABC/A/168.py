N = input()
hon = "24579"
pon = "0168"
bon = "3"
if N[-1] in hon:
  print("hon")
elif N[-1] in pon:
  print("pon")
else:
  print("bon")