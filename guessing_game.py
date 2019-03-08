import sys

def main():
  guess = True
  lower, upper = 0,11
  curr = 0
  for line in sys.stdin:
    line = line.strip()
    if guess:
      curr = int(line)
    else:
      if line == "too high":
        upper = min(upper,curr)
      elif line == "too low":
        lower = max(lower, curr)
      else:
        if lower < curr < upper:
          print "Stan may be honest"
        else:
          print "Stan is dishonest"
        lower, upper = 0,11
    guess = not guess

if __name__ == '__main__':
  main()
