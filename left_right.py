import sys

def main():
  n = int(sys.stdin.readline().strip())
  curr = 0
  cmd = sys.stdin.readline().strip()
  last = "R"
  count = 1
  for i in cmd:
    if i == last:
      count += 1
    else:
      if last == "R":
        for j in xrange(count-1):
          curr +=1
          print curr
      else:
        curr += count+1
        for j in xrange(count+1):
          print curr - j
      last = i
      count = 1

  remain = xrange(n,curr, -1) if last=="L" else xrange(curr+1,n+1)
  for k in remain:
    print k

if __name__ == '__main__':
  main()

