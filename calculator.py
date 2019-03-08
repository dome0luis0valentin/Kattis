import sys

NUMS = set("0123456789")
def getNum(expr, init = ""):
  num =[init]
  while len(expr) > 0:
    if expr[-1] in NUMS:
      num.append(expr.pop())
    else:
      break
  return int("".join(num))

ops = {"*" : 2, "/": 2, "+": 1, "-": 1}

def compute(left,op,right,preds):
  preds.pop()
  if op == "+":
    return right+left
  elif op == "-":
    return left-right
  elif op == "*":
    return left*right
  return left/float(right)

def reduce_stack(stack, preds):
  token = stack.pop()
  if token == ")":
    right = stack.pop()
    op = stack.pop()
    if op == "(":
      stack.append(right)
      return
    left = stack.pop()
    n = compute(left,op,right,preds)
    last = stack.pop()
    while (last != "(" and len(stack) > 1):
      right = n
      op = last
      left = stack.pop()
      n = compute(left,op,right,preds)
      last = stack.pop()
  else:
    right = token
    op = stack.pop()
    left = stack.pop()
    n = compute(left,op,right,preds)
  stack.append(n)

def parse(line):
  preds = [(-1,0)]
  stack = []
  expr = [i for i in reversed(line) if i.strip() != ""]
  level = 0
  last_op = True
  while len(expr) > 0:
    token = expr.pop()
    if token in NUMS or (last_op and token in "-+"):
      stack.append(getNum(expr, token))
      last_op = False
    elif token == ")":
      level -= 1
      last_op = False
      stack.append(")")
      reduce_stack(stack, preds)
    elif token == "(":
      last_op = True
      level +=1
      stack.append(token)
    elif token in ops:
      last_op = True
      pred = (level, ops[token])
      while pred <= preds[-1]:
        reduce_stack(stack,preds)
      stack.append(token)
      preds.append(pred)

  while (len(stack) > 2):
    reduce_stack(stack, preds)

  return stack[-1]

def main():
  for line in sys.stdin:
    line = line.strip()
    if line != "":
      print "{:.2f}".format(parse(line))

if __name__ == '__main__':
  main()
