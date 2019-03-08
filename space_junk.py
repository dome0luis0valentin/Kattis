import sys,math

def quadratic_roots(a,b,c):
  if a == 0:
    return []
  d = b*b - (4*a*c)
  if d < 0:
    return []
  d_sqrt = math.sqrt(d)
  return ((-1*b - d_sqrt)/(2*a), (-1*b + d_sqrt)/(2*a))

def main():
  cases = int(sys.stdin.readline().strip())

  for i in xrange(cases):
    x1,y1,z1,r1,v1x,v1y,v1z = [int(i) for i in sys.stdin.readline().split()]
    x2,y2,z2,r2,v2x,v2y,v2z = [int(i) for i in sys.stdin.readline().split()]

    dx,dy,dz = x1-x2, y1-y2, z1-z2
    dvx, dvy, dvz = v1x - v2x, v1y - v2y, v1z - v2z
    k = (r1+r2)**2
    c = dx*dx + dy*dy + dz*dz
    b = 2*(dx*dvx + dy*dvy + dz*dvz)
    a = dvx*dvx + dvy*dvy + dvz*dvz
    roots = [i for i in quadratic_roots(a,b,c-k) if i>0]
    if len(roots) == 0:
      print "No collision"
    else:
      print "{0:.4f}".format(roots[0])

if __name__ == '__main__':
  main()
