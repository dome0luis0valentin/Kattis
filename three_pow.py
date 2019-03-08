import sys

def main():
  n = int(sys.stdin.readline().strip())
  while n!=0:
    sub_set = []
    count = 0
    for i in reversed(bin(n-1)[2:]):
      if i=='1':
        sub_set.append(str(pow(3,count)))
      count += 1
    if len(sub_set) == 0:
      print "{ }"
    else:
      print "{ " + ", ".join(sub_set) + " }"
    n = int(sys.stdin.readline().strip())

if __name__ == '__main__':
  main()
