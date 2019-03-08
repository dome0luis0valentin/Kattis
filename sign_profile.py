import sys,math

def quadratic_roots(a,b,c):
  D = b*b - 4.0*a*c
  if D<0:
    return [0]
  elif a==0:
    if b !=0:
      return [(-1*c)/b]
    else:
      return []
  elif D==0:
   return [(-1.0*b)/(2.0*a)]
  else:
    D = math.sqrt(D)
    r1 = (-1.0*b + D)/(2.0*a)
    r2 = (-1.0*b - D)/(2.0*a)
    return [r1,r2] if r1 < r2 else [r2,r1]

def condense(signs):
  if len(signs) == 0:
    return []
  final_signs = [signs[0]]
  for i in signs[1:]:
    if i != final_signs[-1]:
      final_signs.append(i)
  return final_signs

def sign_profile(c):
  if c[2] == c[3] == 0: # have line
    if c[1] == 0: # horizontal line
      print "-" if c[0] < 0 else "+"
    else:
      print "-+" if c[1] > 0 else "+-"
    return

  f = lambda x : sum([c[i]*(x**i) for i in xrange(4)])
  # x coordinate of point changing from increasing to decreasing
  peaks_x = quadratic_roots(3*c[3], 2*c[2], c[1])
  peaks_y = [ f(x) for x in peaks_x ]
  e = 1E-6

  # add behavior as x-> -infinity
  if f(peaks_x[0]-1) > peaks_y[0]:
    signs = ["+"]
  else:
    signs = ["-"]

  signs += ["-" if y < 0 else "+" for y in peaks_y]

  # add behavior as x-> infinity
  if f(peaks_x[-1]+1) > peaks_y[-1]:
    signs.append("+")
  else:
    signs.append("-")

  print "".join(condense(signs))

def main():
  for line in sys.stdin:
    if line.strip() == "0 0 0 0":
      break
    coeff = [float(i) for i in line.strip().split()]
    sign_profile(coeff)

if __name__ == '__main__':
  main()
