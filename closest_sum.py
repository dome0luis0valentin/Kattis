import sys

def closest_sum(nums,q):
  i,j = 0, len(nums)-1
  s = nums[i] + nums[j]
  closest_sofar = s
  while i<j:
    s = nums[i] + nums[j]
    if abs(q-s) < abs(q-closest_sofar):
      closest_sofar = s
    if q == s:
      return q
    elif q < s:
      j -= 1
    else:
      i +=1
  return closest_sofar

def main():
  line = lambda : sys.stdin.readline().strip()
  n = line()
  case = 1
  while n:
    n = int(n)
    nums = [int(line()) for i in xrange(n)]
    nums.sort()
    m = int(line())
    print "Case {}:".format(case)
    for i in xrange(m):
      q = int(line())
      close = closest_sum(nums,q)
      print "Closest sum to {} is {}.".format(q,close)
    n = line()
    case +=1

if __name__ == '__main__':
  main()
