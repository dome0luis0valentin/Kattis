import sys,math

def nametag(n):
  char = "abcdefghijklmnopqrstuvwxyz"
  if n<=25:
    print "a{}".format(char[n])
    return

  name = [0] # always start with a
  remains = n %25
  second_letter = 25 - ((25 - remains) / 2 if remains else 0)
  name.append(second_letter)
  turn = 0
  n -= abs(name[1] - name[0])
  while (n > 25):
    if turn%2:
      name.append(25)
    else:
      name.append(0)
    turn +=1
    n -= abs(name[-2] - name[-1])

  if name[-1] == 0:
    name.append(n)
  else:
    name.append(name[-1] - n)

  print "".join([char[i] for i in name])

def main():
  nametag(int(sys.stdin.readline().strip()))

if __name__ == '__main__':
  main()
