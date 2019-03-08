import sys,math

def point_of_contact(p1,p2,p3,r):
  xa, ya = p1
  xb, yb = p2
  cx, cy = p3
  dx, dy = xa-cx, ya-cy
  n = xb**2 + yb**2
  m = 2*(dx*xb + dy*yb)
  p = dx**2 + dy**2 - (4*(r**2))

  D = m*m - 4*n*p
  if D < 0:
    return False

  t1 = (math.sqrt(D) - m)/(2*n)
  t2 = (-1.0*math.sqrt(D) - m)/(2*n)
  if max(t1,t2) < 0:
    return False
  if t1 < 0:
    t = t2
  elif t2 < 0:
    t = t1
  else:
    t = min(t1,t2)

  px, py = xa + t*xb, ya + t*yb
  return (t,px,py)

def main():
  p1 = [int(i) for i in sys.stdin.readline().split()]
  p2 = [int(i) for i in sys.stdin.readline().split()]
  p3 = [int(i) for i in sys.stdin.readline().split()]
  vx, vy, r = [int(i) for i in sys.stdin.readline().split()]

  v = (vx,vy)

  poc_12 = point_of_contact(p1,v, p2, r)
  poc_13 = point_of_contact(p1,v, p3, r)
  contact_order = []
  if poc_12 and ((not poc_13) or (poc_12[0] < poc_13[0])):
    contact_order.append(2)
    mv_dir = (p2[0] - poc_12[1], p2[1] - poc_12[2])
    poc_last = point_of_contact(p2,mv_dir,p3,r)
    if poc_last:
      contact_order.append(3)
  elif poc_13:
    contact_order.append(3)
    mv_dir = (p3[0] - poc_13[1], p3[1] - poc_13[2])
    poc_last = point_of_contact(p3,mv_dir,p2,r)
    if poc_last:
      contact_order.append(2)

  if contact_order == [2,3]:
    print 1
  elif contact_order == [3,2]:
    print 2
  elif contact_order == [2]:
    print 3
  elif contact_order == [3]:
    print 4
  else:
    print 5

if __name__ == '__main__':
  main()
