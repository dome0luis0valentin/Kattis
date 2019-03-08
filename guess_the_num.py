import sys
from itertools import permutations

def get_vars(eq):
  vars_sofar = set()
  ops = set(list("+*-()"))
  for i in eq:
    if i not in ops:
      vars_sofar.add(i)
  if len(vars_sofar) == 1:
    return vars_sofar.pop()+","
  return ",".join(vars_sofar)

def check(eq,vals,result):
  variables = get_vars(eq)
  for i in permutations(vals):
    exec("{0} = {1}; res = {2}".format(variables,i,eq))
    if res == result:
      print "YES"
      return
  print "NO"


def main():
  nums = [int(i) for i in sys.stdin.readline().split()]
  while nums[0] > 0:
    eq = sys.stdin.readline().strip()
    vals = nums[1:-1]
    res = nums[-1]
    check(eq, vals, res)
    nums = [int(i) for i in sys.stdin.readline().split()]

if __name__ == '__main__':
  main()
