import sys
def fact(n):
  facts = [1]
  for i in xrange(1,n+1):
    facts.append(facts[-1]*i)
  return facts

FACTS = fact(50)
def kth_perm(nums,k):
  if (k==0):
    return nums
  sub = FACTS[len(nums)-1]
  bucket = k/sub
  rest = kth_perm( nums[:bucket] + nums[bucket+1:], k%sub)
  return [nums[bucket]] + rest


def main():
  for line in sys.stdin:
    n,k = [int(i) for i in line.split()]
    facts = fact(n)
    print " ".join(kth_perm([str(i) for i in range(1,n+1)],k))

if __name__ == "__main__":
  main()
