import sys

def polygonArea(X,Y):
  n = len(X)
  area = 0.0
  j = n-1 # prev
  for i in range(n):
    area += (X[j] + X[i]) * (Y[j] - Y[i])
    j = i
  return abs(area)/2.0

def separator(px,py,nx,ny,sign):
  c1 = px*px - nx*nx
  c2 = nx-px
  c3 = ny*ny - py*py
  c4 = py-ny

  a,b,c = 2*c2, -2*c4, c1-c3

  if sign == "Hotter":
    sep = lambda x,y : (a*x + b*y + c) > 0
  elif sign == "Colder":
    sep = lambda x,y : (a*x + b*y + c) < 0
  else:
    sep = lambda x,y : (a*x + b*y + c) ==  0
  
  return sep,(a,b,c)

def intersection(l1,x1,y1,x2,y2):
  a1,b1,c1 = l1
  a,b,c = y1-y2,x2-x1, (y2-y1)*x1 + (x1-x2)*y1
  if a == 0:
    y = (-1.0*c)/b
    x = (b1*y + c1)/(-1.0*a1)
  elif a1 == 0:
    y =(-1.0*c1)/b1
    x = (b*y + c)/(-1.0*a)
  elif b == 0:
    x = (-1.0*c)/a
    y = (a1*x + c1)/(-1.0*b1)
  elif b1 == 0:
    x = (-1.0*c1)/a1
    y = (a*x + c)/(-1.0*b)
  else: # General case
    y = (a*c1 - a1*c)/(1.0*(a1*b - a*b1))
    x = (b*y + c)/(-1.0*a)
  return x,y
     

def main():
  X = [0.0,0.0,10.0,10.0]
  Y = [0.0,10.0,10.0,0.0]
  px, py = (0.0, 0.0)
  validA = 100  
  for line in sys.stdin:
    nx,ny,sign = line.strip().split()
    nx,ny,sign = float(nx), float(ny), sign
    n = len(X)
    if sign == "Same" or n<3 or validA==0:
      validA = 0
    else:
      sep,line = separator(px,py,nx,ny,sign)
      newX,newY = [],[]
      parity = [sep(x,y) for x,y in zip(X,Y)]
      j = n-1 # prev
      for i in xrange(n):
        if parity[i] != parity[j]:
          inter_x, inter_y = intersection(line,X[i],Y[i],X[j],Y[j])
          newX.append(inter_x)
          newY.append(inter_y)
        if parity[i]:
          newX.append(X[i])
          newY.append(Y[i])
        j = i
      X,Y = newX,newY
      validA = polygonArea(X,Y)

    print "%.6f" % validA
    px,py = nx,ny

if __name__ == '__main__':
  main()

