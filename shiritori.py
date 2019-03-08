import sys

def main():
  n = int(sys.stdin.readline().strip())
  seen = set()
  player = 1
  prev = ""
  for line in sys.stdin:
    word = line.strip()
    if prev == "" or (prev == word[0] and word not in seen):
      player += 1
      prev = word[-1]
      seen.add(word)
    else:
      break
  if player%2 == 0:
    player = 2
  else:
    player = 1

  if len(seen) == n:
    print "Fair game"
  else:
    print "Player {}  lost".format(player)

if __name__ == '__main__':
  main()
