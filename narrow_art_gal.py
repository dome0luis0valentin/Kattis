import sys

def min_cost(gallery, r,k, side=0, ans = {}):
  if (r,k,side) in ans:
    return ans[(r,k,side)]
  if k > r+1:
    return 40000
  if k == 0:
    return 0
  v1 = min_cost(gallery, r-1, k, 0, ans)
  if side == 0:
    v2 = gallery[r][0] + min_cost(gallery, r-1, k-1, -1, ans)
    v3 = gallery[r][1] + min_cost(gallery, r-1, k-1, 1, ans)
    v = min(v1,v2,v3)
  elif side == -1:
    v2 = gallery[r][0] + min_cost(gallery, r-1, k-1, -1, ans)
    v = min(v1,v2)
  else:
    v3 = gallery[r][1] + min_cost(gallery, r-1, k-1, 1, ans)
    v = min(v1,v3)
  ans[(r,k,side)] = v
  return v



def main():
  intList = lambda : [int(i) for i in sys.stdin.readline().split()]
  n, k = intList()
  while not(0 == n == k):
    gallery = []
    total = 0
    for i in xrange(n):
      row = intList()
      total += (row[0]+row[1])
      gallery.append(row)
    print total -  min_cost(gallery, n-1 ,k)
    n, k = intList()

if __name__ == '__main__':
  main()
