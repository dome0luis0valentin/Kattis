import sys

def main():
  n = int(sys.stdin.readline().strip())
  nums = [-1] + map(lambda x: int(x)%2 , sys.stdin.readline().split()) + [-2]
  pointers = [(i+1) for i in xrange(n+2)]
  prev_l,curr_l = 0,n
  while (prev_l != curr_l):
    prev_l = curr_l
    prev, at = 0,pointers[0]
    while (at <= n):
      nxt = pointers[at]
      if nums[at] == nums[nxt]:
        at = pointers[nxt]
        pointers[prev] = at
        curr_l -= 2
      else:
        prev, at = at, nxt
  print curr_l

if __name__ == '__main__':
  main()

