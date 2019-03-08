import sys

def main():
  n = int(sys.stdin.readline().strip())
  nums = []
  
  for i in xrange(n):
    sid = int(sys.stdin.readline().strip())
    nums.append(sid)
 
  m = n
  while True:
    modulo = set()
    for i in nums:
      val = i%m
      if val in modulo:
        break
      else:
        modulo.add(val)

    if len(modulo) == n:
      print m
      break
    else:
      m +=1


if __name__ == '__main__':
  main()
