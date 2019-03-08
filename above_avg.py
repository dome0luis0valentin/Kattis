import sys

def main():
  cases = int(sys.stdin.readline().strip())
  for line in sys.stdin:
    line = [int(i) for i in line.split()]
    n, grades = line[0]*1.0, line[1:]
    avg = reduce(lambda x,y: x+y, grades)
    above_avg = len(filter(lambda x: x*n > avg,grades))*100
    print "{:.3f}%".format(above_avg/n)

if __name__ == '__main__':
  main()
