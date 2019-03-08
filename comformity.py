import sys
import bisect as bi

def main():
  n = int(sys.stdin.readline().strip())
  counts = {}
  for line in sys.stdin:
    courses = tuple(sorted([int(c) for c in line.split()]))
    if courses in counts:
      counts[courses] += 1
    else:
      counts[courses] = 1
  freq = sorted(counts.values())
  start = freq[-1]
  total = start*(len(freq) - bi.bisect_left(freq,start))
  print total

if __name__ == '__main__':
  main()
