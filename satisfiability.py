import sys

def works(clauses, assignment):
  for c in clauses:
    val = False
    for v in c:
      if len(v) == 1:
        val |= assignment & (1<<v[0])
      else:
        val |= not(assignment & (1<<v[0]))
    if not val:
      return False
  return True


def main():
  line = lambda : sys.stdin.readline()
  cases = int(line().strip())
  for c in xrange(cases):
    n,m = map(int, line().split())
    clauses = []
    for k in xrange(m):
      clause = line().strip().split("v")
      for i in xrange(len(clause)):
        var = clause[i].strip()
        if var[0] == "~":
          index = int(var[2:])-1
          clause[i] = [index, "~"]
        else:
          index = int(var[1:])-1
          clause[i] = [index]

      clauses.append(clause)

    flag = True
    for assignment in xrange(1<<n):
      if works(clauses, assignment):
        print "satisfiable"
        flag = False
        break
    if flag:
      print "unsatisfiable"

if __name__ == '__main__':
  main()
