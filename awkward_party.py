import sys

def main():
  l = lambda : sys.stdin.readline().strip()
  n = int(l())
  guests = map(int, l().split())
  lang_diffs = {}
  for i,g in enumerate(guests):
    if g in lang_diffs:
      lang_diffs[g].append(i)
    else:
      lang_diffs[g] = [i]

  awk_lvl = n
  for k in lang_diffs:
    lang = lang_diffs[k]
    min_diff = n
    for i in xrange(1,len(lang)):
      d = lang[i] - lang[i-1]
      if d < min_diff:
        min_diff = d
    if min_diff < awk_lvl:
      awk_lvl = min_diff
  print awk_lvl

if __name__ == '__main__':
  main()
