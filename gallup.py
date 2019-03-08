import sys

def main():
  case = 1
  for line in sys.stdin:
    if line.strip() == "0":
      break
    line = line.split()
    n, nums = int(line[0]), line[1:]
    decimals = 0 if "." not in nums[0] else len(nums[0].split(".")[-1])
    nums = [ round(i, decimals) for i in map(float, nums) ]
    k = 1
    s = round(sum(nums),0)
    while k < 10000:
      v = [ round((i*k)/s, 0) for i in nums]
      if sum(v) != k:
        k += 1
        continue
      np = [ round((i*100)/k, decimals) for i in v]
      not_valid = False
      for new,old in zip(np, nums):
        if new != old:
          not_valid = True
          break
      if not_valid:
        k+=1
        continue
      break
    k = k if k < 10000 else "error"
    print "Case {}: {}".format(case, k)
    case +=1

if __name__ == '__main__':
  main()
