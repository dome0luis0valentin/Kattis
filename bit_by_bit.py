import sys

def main():
  while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
      break
    bits = [-1 for i in xrange(32)]
    for i in xrange(n):
      cmd = sys.stdin.readline().split()
      if cmd[0] == "SET":
        bits[int(cmd[1])] = 1
      elif cmd[0] == "CLEAR":
        bits[int(cmd[1])] = 0
      elif cmd[0] == "OR":
        a,b = int(cmd[1]), int(cmd[2])
        if bits[a] == 1 or bits[b] == 1:
          bits[a] = 1
        elif bits[a] == 0 and bits[b] == 0:
          bits[a] = 0
        else:
          bits[a] = -1
      else:
        a,b = int(cmd[1]), int(cmd[2])
        if bits[a] == 0 or bits[b] == 0:
          bits[a] = 0
        elif bits[a] == 1 and bits[b] == 1:
          bits[a] = 1
        else:
          bits[a] = -1
    print "".join(map(lambda x: "?" if x == -1 else str(x), reversed(bits)))

if __name__ == '__main__':
  main()
