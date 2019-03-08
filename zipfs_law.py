import sys
from collections import defaultdict

def main():
  EOT = "EndOfText"
  newStart = True
  veryFirst = True
  for line in sys.stdin:
    if newStart:
      if not veryFirst:
        print
      n = int(line.strip())
      word_map = defaultdict(int)
      newStart = False
      veryFirst = False
    elif EOT == line.strip():
      to_print = []
      for i in word_map:
        if word_map[i] == n:
          to_print.append(i)
      to_print.sort()
      for i in to_print:
        print i
      if len(to_print) == 0:
        print "There is no such word."
      newStart = True
    else:
      word = []
      for i in line:
        if i.isalpha():
          word.append(i.lower())
        else:
          w = "".join(word)
          word_map[w] += 1
          word = []

if __name__ == '__main__':
  main()
