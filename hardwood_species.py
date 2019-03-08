import sys

def main():
  hardwoods = {}
  total = 0.0
  for line in sys.stdin:
    line = line.strip()
    if line in hardwoods:
      hardwoods[line] += 1
    else:
      hardwoods[line] = 1
    total += 1
  for i in sorted(hardwoods.keys()):
    print i, (hardwoods[i]*100)/total

if __name__ == '__main__':
  main()
