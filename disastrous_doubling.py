import sys

def main():
  n = int(sys.stdin.readline().strip())
  reqs = (int(i) for i in sys.stdin.readline().split())
  avail = 1
  for i in reqs:
    avail *= 2
    if i > avail:
      print "error"
      return
    else:
      avail -= i
  print avail % (10**9 +7)

if __name__ == '__main__':
  main()
