import sys

def main():
  n = sys.stdin.readline()
  num = []
  for line in sys.stdin:
    c = line.strip()
    num.append('0' if c == 'Z' else '1')
  print int("".join(num),2)

if __name__ == '__main__':
  main()
