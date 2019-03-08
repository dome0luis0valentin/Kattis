import sys

valid_ints = set([str(i) for i in xrange(-10,11)])

def simplify(exp):
  if len(exp) == 0:
    return ""
  token = exp.pop()
  if token not in  "*+-":
    if token in valid_ints:
      return int(token)
    return token
  else:
    exp1 = simplify(exp)
    exp2 = simplify(exp)
    if type(exp1) == type(exp2) == type(1):
        return eval("{} {} {}".format(exp1, token, exp2))
    return "{} {} {}".format(token, exp1, exp2)

def main():
  case = 1
  for line in sys.stdin:
    print "Case {}: {}".format(case, simplify(list(reversed(line.split()))))
    case +=1

if __name__ == '__main__':
  main()
