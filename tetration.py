import sys

def main():
  n = float(sys.stdin.readline().strip())
  print "%.6f" % n**(1/n)

if __name__ == '__main__':
  main()
