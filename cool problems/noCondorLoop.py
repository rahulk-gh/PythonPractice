# take 3 inputs, x, hi and lo.  When  outside the hi and lo give back hi if above hi and lo if below low.  if within the range give back  x . DO NOT USE CONDITIONALS 

x = 3
hi = 10
lo = 1

def clip ( lo, x, hi):
  return ( min (max(x, lo) , hi))

clip ( lo, x, hi ) 
