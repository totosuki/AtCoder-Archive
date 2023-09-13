N = int(input())
left = 1
right = N

while right - left > 1:
  mid = (left + right) // 2
  print(f"? {mid}", flush = True)
  Si = int(input())
  
  if Si == 1:
    right = mid
  else:
    left = mid

print(f"! {left}")