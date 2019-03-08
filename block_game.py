import sys

def who_wins(a,b,player):
  a,b = (a,b) if a <= b else (b,a)
  while(b%a != 0 and b/a == 1):
    a,b = b%a, a
    player *= -1
  return player


def main():
  a,b = [int(k) for k in sys.stdin.readline().split()]
  if (who_wins(a,b,1) == 1):
    print "win"
  else:
    print "lose"

if __name__ == '__main__':
  main()
