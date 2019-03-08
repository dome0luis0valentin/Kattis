import sys

def main():
  s, k = sys.stdin.readline().split()
  s, k = list(s), int(k)
  n = len(s)
  if k <= n/2:
    print "Yes"
  else:
    ss = sorted(s)
    start = n-k
    if ss[start:k] == s[start:k]:
      print "Yes"
    else:
      print "No"

if __name__ == '__main__':
  main()
