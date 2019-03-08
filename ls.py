import sys

def match(pattern,string):
  patterns = [i for i in pattern.split("*") if i!='']

  if len(patterns) == 0:
    return True

  if pattern[0] != '*':
    if string.startswith(patterns[0]):
      string = string[len(patterns[0]):]
      patterns = patterns[1:]
      if len(patterns) == 0:
        return True
    else:
      return False
  if pattern[-1] != '*':
    if string.endswith(patterns[-1]):
      string = string[ : -1*len(patterns[-1])]
      patterns = patterns[:-1]
    else:
      return False

  i = 0
  for p in patterns:
    i = string.find(p,i)
    if i==-1:
      return False
    i += len(p)
  return True

def main():
  pattern = sys.stdin.readline().strip()
  next(sys.stdin)
  for line in sys.stdin:
    line = line.strip()
    if match(pattern, line):
      print line

if __name__ == '__main__':
  main()
