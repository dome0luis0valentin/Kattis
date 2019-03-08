import sys, heapq

def distribute(city_pop,b,c):
    city_pop = [ (-1*k, k, 1) for k in city_pop]
    b -= c
    heapq.heapify(city_pop)
    while b > 0:
      _,p,n = heapq.heappop(city_pop)
      n += 1
      if p % n == 0:
        pop_perB = p/n
      else:
        pop_perB = (p/n)+1
      heapq.heappush(city_pop,(-1*pop_perB,p,n))
      b -= 1

    return heapq.heappop(city_pop)[0]*-1

def is_valid_max(city_pop,max_p,max_ballots):
  ballots_needed = 0
  for i in city_pop:
    q,r = divmod(i,max_p)
    ballots_needed += q
    if r > 0:
      ballots_needed += 1
    if ballots_needed > max_ballots:
      return False
  return ballots_needed <= max_ballots


def distribute_2(city_pop,b,c):
  start, end = 1,5000000

  while (end - start > 1):
    mid = (start + end)/2
    if is_valid_max(city_pop, mid, b):
      end = mid
    else:
      start = mid
  if is_valid_max(city_pop, start, b):
    return start
  return end

def main():
  c,b = [int(i) for i in sys.stdin.readline().split()]
  while c!= -1 and b != -1:
    city_pop = [int(sys.stdin.readline().strip()) for i in xrange(c)]
    print distribute_2(city_pop,b,c)
    sys.stdin.readline()
    c,b = [int(i) for i in sys.stdin.readline().split()]


if __name__ == '__main__':
  main()
