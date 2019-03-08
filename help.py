import sys

def refine(indirects, ph):
  next_indirects = []
  prev_len, curr_len = 0, len(indirects)
  while curr_len > 0:
    if prev_len == curr_len:
      ph[indirects[0][0]] = "hermonwashere"
    for w1,w2 in indirects:
      if w1 in ph and w2 in ph:
        if ph[w1] != ph[w2]:
          return False, {}
      elif w1 in ph:
        ph[w2] = ph[w1]
      elif w2 in ph:
        ph[w1] = ph[w2]
      else:
        next_indirects.append((w1,w2))
    prev_len, curr_len = curr_len, len(next_indirects)
    indirects, next_indirects = next_indirects, []
  return True, ph

def present(ph,s1):
  return " ".join(map(lambda x: x if (x not in ph) else ph[x], s1))

def main():
  line = lambda : sys.stdin.readline().strip()
  n = int(line())
  is_placeholder = lambda s: s[0] == "<" and s[-1] == ">"
  for i in xrange(n):
    inconsistancy = False
    s1 = line().split()
    s2 = line().split()
    if len(s1) != len(s2):
      inconsistancy = True
    else:
      placeholder = {}
      indirect_ass = []
      for w1,w2 in zip(s1,s2):
        if is_placeholder(w1) and not is_placeholder(w2):
          if w1 in placeholder and placeholder[w1] != w2:
            inconsistancy = True
            break
          else:
            placeholder[w1] = w2
        elif is_placeholder(w2) and not is_placeholder(w1):
          w2 = "{}-2".format(w2)
          if w2 in placeholder and placeholder[w2] != w1:
            inconsistancy = True
            break
          else:
            placeholder[w2] = w1
        elif is_placeholder(w1) and is_placeholder(w2):
          w2 = "{}-2".format(w2)
          if w1 in placeholder and w2 in placeholder:
            if placeholder[w1] != placeholder[w2]:
              inconsistancy = True
              break
          elif w1 in placeholder:
            placeholder[w2] = placeholder[w1]
          elif w2 in placeholder:
            placeholder[w1] = placeholder[w2]
          else: # both place holder are not seen before
            if w1 != w2:
              indirect_ass.append((w1,w2))
        else:
          if w1 != w2:
            inconsistancy = True
            break

    if not inconsistancy:
      isok, new_ph = refine(indirect_ass,placeholder)
      if isok:
        print present(new_ph,s1)
      else:
        print "-"
    else:
      print "-"

if __name__ == '__main__':
  main()



