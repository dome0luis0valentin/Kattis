import sys

def main():
  n = int(sys.stdin.readline().strip())
  catagory = []
  maps = []
  all_key = set()
  cats = set()
  for c in xrange(n):
    line = sys.stdin.readline().split()
    catagory.append(line[0])
    m = set()
    for w in line[2:]:
      m.add(w)
      all_key.add(w)
    maps.append(m)

  cat_count = [0 for i in xrange(n)]
  for line in sys.stdin:
    for word in line.split():
      if word in all_key:
        for k,a_set in enumerate(maps):
          if word in a_set:
            cat_count[k] +=1

  max_s = max(cat_count)
  for i,j in enumerate(cat_count):
    if j == max_s:
      cats.add(catagory[i])

  print "\n".join(sorted(list(cats)))

if __name__ == '__main__':
  main()

