import sys

at = 0
def parse(expr,resistors):
  global at
  if len(expr) == 0:
    return []

  exprs = []
  op = ""
  while at < len(expr):
    if expr[at] == "(":
      at += 1
      exp1 = parse(expr, resistors)
      exprs.append(exp1)
    elif expr[at] == "R":
      v = resistors[int(expr[at+1]) - 1]
      exprs.append([v])
      at += 2
    elif expr[at] == ")":
      at += 1
      return [op, exprs]
    elif expr[at] in "|-":
      if op == "":
        op = expr[at]
      at += 1

  return [op, exprs]

def evaluate(expr):
  if len(expr) == 1:
    return expr[0]
  op = expr[0]
  res = 0
  if op == '-':
    for i in expr[1]:
      res += evaluate(i)
    return res
  else:
    for i in expr[1]:
      res += (1.0/evaluate(i))
    return 1.0/res

def main():
  line = lambda : sys.stdin.readline().strip()
  n = int(line())
  resistors = map(float, line().split())
  expr = line()
  expr = parse(list(expr)[1:-1], resistors)
  print "{:.5f}".format(evaluate(expr))

if __name__ == '__main__':
  main()
