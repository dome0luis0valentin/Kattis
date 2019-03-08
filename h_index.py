import sys, bisect

def main():
  n = int(sys.stdin.readline().strip())
  citations = []
  for i in sys.stdin:
    citations.append(int(i.strip()))
  citations.sort(reverse=True)

  curr = 0
  h_index = 0
  for i in xrange(n):
    curr_index = min(citations[i], i+1)
    h_index = max(curr_index, h_index)
  print h_index

if __name__ == '__main__':
  main()
