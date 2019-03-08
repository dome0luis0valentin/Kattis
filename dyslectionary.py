import sys

def sort_print(words,max_width):
  words.sort(key = lambda word: "".join(reversed(word)))
  for w in words:
    print w.rjust(max_width)

def main():
  words = []
  max_width = 0
  for line in sys.stdin:
    line = line.strip()
    if line == "":
      sort_print(words,max_width)
      print
      words = []
      max_width = 0
    else:
      words.append(line)
      max_width = max(max_width,len(line))
  sort_print(words,max_width)

if __name__ == "__main__":
  main()
