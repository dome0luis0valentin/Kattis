import sys,math

def dot(x,y):
  # Dot product with Kahan floating point summation,
  #to avoid catastrophic cancelation
  total  = 0.0
  compensation = 0.0
  for (e1,e2) in zip(x,y):
    val = e1*e2 - compensation
    new_sum = total + val
    compensation = (new_sum - total) - val
    total = new_sum
  return total


def main():
  dim = int(sys.stdin.readline().strip())
  w_b = [float(i) for i in sys.stdin.readline().split()]
  w,b = w_b[:-1], w_b[-1]
  norm = math.sqrt(dot(w,w))
  for line in sys.stdin:
    v = [ float(i) for i in line.split() ]
    print "%.5f"% ((dot(w,v) + b)/norm)

if __name__ == '__main__':
  main()
