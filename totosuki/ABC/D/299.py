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

# Code Golf
# l=1
# r=int(input())
# while r-l>1:
#  print("?",m:=(l+r)//2)
#  if input()>"0":r=m
#  else:l=m
# print("!",l)