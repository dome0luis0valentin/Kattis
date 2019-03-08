import sys

def main():
  line = sys.stdin.readline().strip()
  moves = { "R":"S", "B":"K", "L":"H" }
  counter = []
  i = 0
  while i < len(line)-2:
    m1,m2,m3 = line[i],line[i+1], line[i+2]
    if m1 != m2 and m2 != m3 and m3 != m1:
      counter.append("C")
      i +=3
    else:
      counter.append(moves[m1])
      i +=1
  while i < len(line):
    counter.append(moves[line[i]])
    i += 1
  print "".join(counter)

if __name__ == '__main__':
  main()

