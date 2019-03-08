from itertools import permutations
def help(seq):
  g = [seq[0]]
  for i in seq[1:]:
    if i>g[-1]:
      g.append(i)
  return g
def gls(gs,s):
  count = 0
  for i in permutations(s):
    if i[0] == gs[0] and help(i) == gs:
      print i
      count +=1
  return count

