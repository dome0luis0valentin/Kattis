import sys,math

def point_of_contact(p1,p2,p3,r):
  xa, ya = p1
  xb, yb = p2
  xc, yc = p3

  m = ((yb-ya)*1.0)/(xb-xa)
  m2 = ((yb-yc)*1.0)/(xb-xc)
  if m2 > m:
    m += (m/90.0)
  elif m2 < m:
    m -= (m/90.0)
  b = yb - m*xb
  k = b-yc

  p, q, s = (m*m)+1, 2*(m*k - xc), xc*xc + k*k - (4*r*r)
  D = q*q - (4*p*s)
  if D < 0:
    return False

  x1 = ((-1.0*q) + math.sqrt(D))/(2.0*p)
  x2 = ((-1.0*q) - math.sqrt(D))/(2.0*p)
  move_dir = xb - xa
  x1_dir = move_dir * (x1 - xa)
  x2_dir = move_dir * (x2 - xa)
  if x1_dir > 0 and x2_dir < 0:
    x = x1
  elif x1_dir > 0 and x2_dir > 0:
    x = min(x1,x2)
  elif x1_dir < 0 and x2_dir > 0:
    x = x2
  else:
    return False
  return (x, m*x+b)

def main():
  p1 = [float(i) for i in sys.stdin.readline().split()]
  p2 = [float(i) for i in sys.stdin.readline().split()]
  p3 = [float(i) for i in sys.stdin.readline().split()]
  vx, vy, r = [float(i) for i in sys.stdin.readline().split()]

  v = (p1[0]+vx, p1[1]+vy)

  poc_12 = point_of_contact(p1,v, p2, r)
  poc_13 = point_of_contact(p1,v, p3, r)

  contact_order = []
  if poc_12 and ((not poc_13) or (abs(poc_12[0]-p1[0]) < abs(poc_13[0]-p1[0]))):
    contact_order.append(2)
    poc_last = point_of_contact(poc_12,p2,p3,r)
    if poc_last:
      contact_order.append(3)
  elif poc_13:
    contact_order.append(3)
    poc_last = point_of_contact(poc_13,p3,p2,r)
    if poc_last:
      contact_order.append(2)

  if contact_order == [2,3]:
    print (1)
  elif contact_order == [3,2]:
    print (2)
  elif contact_order == [2]:
    print (3)
  elif contact_order == [3]:
    print (4)
  else:
    print (5)

if __name__ == '__main__':
  main()
