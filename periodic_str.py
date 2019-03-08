import sys

line = sys.stdin.readline().strip()
n = len(line)
def check_period(k):
  prev = line[:k]
  for i in xrange(k, n, k):
   if (prev == line[i+1:i+k]+line[i]):
     prev = line[i:i+k]
   else:
     return False
  return True

def main():
  for i in xrange(1,n+1):
    if (n%i == 0 and check_period(i)):
      print i
      break

if __name__ == "__main__":
  main()
