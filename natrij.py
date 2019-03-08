import sys

def main():
  line = lambda : sys.stdin.readline().strip()
  start = [int(i) for i in line().split(":")]
  end = [int(i) for i in line().split(":")]
  start = start[0]*3600 + start[1]*60 + start[2]
  end = end[0]*3600 + end[1]*60 + end[2]
  if end <= start:
    end += 24*3600
  diff = end - start
  hr, rest = divmod(diff,3600)
  mi, sec = divmod(rest, 60)
  print "{:0>2d}:{:0>2d}:{:0>2d}".format(hr,mi,sec)

if __name__ == '__main__':
  main()
