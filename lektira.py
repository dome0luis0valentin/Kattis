import sys

def smallest(word):
  min_sofar = word
  n = len(word)
  for i in xrange(1,n+1):
    for k in xrange(i+1, n):
      parts = [word[:i],word[i:k], word[k:]]
      new_w = "".join(["".join(reversed(w)) for w in parts])
      if new_w < min_sofar:
        min_sofar = new_w
  print min_sofar

def main():
  smallest(sys.stdin.readline().strip())

if __name__ == '__main__':
  main()
