import sys

def solve(m):
  det_inv = m[0][0]*m[1][1] - m[0][1]*m[1][0]
  print m[1][1]/det_inv, (m[0][1]*-1)/(det_inv)
  print (-1*m[1][0])/det_inv, m[0][0]/det_inv

def main():
  matrix= []
  case_num = 1
  for line in sys.stdin:
    line = line.strip()
    if line == "":
      print "Case {0}:".format(case_num)
      solve(matrix)
      matrix = []
      case_num +=1
    else:
      matrix.append([int(i) for i in line.split()])

if __name__ == "__main__":
  main()
