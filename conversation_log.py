import sys

def main():
  getline = lambda : sys.stdin.readline().strip()
  n = int(getline())
  words = {}
  users = set()
  for i in xrange(n):
    w = getline().split()
    user, msg = w[0], w[1:]
    for m in msg:
      if m in words:
        words[m][0] += 1
        words[m][1].add(user)
      else:
        words[m] = [1, set([user])]
    users.add(user)
  # Now identify what to print
  all_users = len(users)
  pairs = [(words[i][0]*-1,i) for i in words if len(words[i][1]) == all_users ]
  for _,w in sorted(pairs):
    print w
  if len(pairs) == 0:
    print "ALL CLEAR"

if __name__ == '__main__':
  main()
