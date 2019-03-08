import sys

def main():
  n = int(sys.stdin.readline())
  gid = []
  for line in sys.stdin:
    for num in line.split():
      num = int(num)
      if len(gid) == 0 or num > gid[-1]:
        gid.append(num)
  print len(gid)
  print " ".join(map(str,gid))

if __name__ == '__main__':
  main()
