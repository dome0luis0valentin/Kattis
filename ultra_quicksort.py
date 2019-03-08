import sys,bisect as b

def count(nums):
  if len(nums) <= 1:
    return 0,nums
  
  mid = len(nums)/2
  firstHalf = nums[:mid]
  secondHalf = nums[mid:]
  c1,sortedFH = count(firstHalf)
  c2,sortedSH = count(secondHalf)

  final = []
  i,j = 0,0
  totalC = c1+c2
  l1 = len(firstHalf)
  fh_done,sh_done = False,False

  while (len(final) < len(nums)):
    if sortedFH[i] > sortedSH[j]:
      final.append(sortedSH[j])
      totalC += (l1-i)
      j+=1 
      if j == len(sortedSH):
        sh_done = True
        break
    else:
      final.append(sortedFH[i])
      i+=1 
      if i == len(sortedFH):
        fh_done = True
        break

  if fh_done:
    for k in xrange(j,len(sortedSH)):
      final.append(sortedSH[k])
  elif sh_done:
    for k in xrange(i,l1):
      final.append(sortedFH[k])

  return totalC,final


def main():
  sys.stdin.readline()
  nums = []
  for line in sys.stdin:
    nums.append(int(line.strip()))
  print count(nums)[0]

if __name__ == '__main__':
  main()
