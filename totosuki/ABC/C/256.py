h1, h2, h3, w1, w2, w3 = map(int, input().split())
rslt = 0
check_nums = tuple(range(1, 29))

for lu in check_nums:
  for ru in check_nums:
    for cc in check_nums:
      for ld in check_nums:
        cu = h1 - (lu + ru)
        lc = w1 - (lu + ld)
        rc = h2 - (lc + cc)
        cd = w2 - (cu + cc)
        rd = h3 - (ld + cd)
        flag = True
        
        if any([lu<1, cu<1, ru<1, lc<1, cc<1, rc<1, ld<1, cd<1, rd<1]):
          flag = False
        if w3 != (ru + rc + rd):
          flag = False
        
        if flag:
          rslt += 1

print(rslt)