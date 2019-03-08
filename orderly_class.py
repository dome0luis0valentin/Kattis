import sys

def main():
  s1 = sys.stdin.readline().strip()
  s2 = sys.stdin.readline().strip()
  n = len(s1)
  left, right = 0, n-1
  while s1[left] == s2[left] and left < n:
    left += 1
  while s1[right] == s2[right] and right >= 0:
    right -=1

  if s1[left:right+1] != "".join(reversed(s2[left:right+1])):
    print 0
    return

  count = 1
  left -= count
  right += count
  while left >= 0 and right < n and s1[left] == s2[right]:
    count +=1
    left -=1
    right += 1
  print count

if __name__ == '__main__':
  main()
