import sys

def main():
  for line in sys.stdin:
    a, op, b = line.split()
    if len(a) > 4:
      a = int(a[-4:])
    else:
      a = int(a)
    if len(b) > 4:
      c = int(b[-4:])
    else:
      c = int(b)
    if op == "+":
      print (a+c) % 10000
    elif op == "*":
      print (a*c) % 10000
    elif op == "^":
      print pow(a,int(b),10000)

if __name__ == '__main__':
  main()
