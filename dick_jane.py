import sys

def main():
  for line in sys.stdin:
    s,p,y,j = [int(i) for i in line.split()]
    a_y = (12 + j - y - p)/3
    a_s = y+a_y
    a_p = p+a_y
    diff = 12+j - (a_s+a_p+a_y)
    if diff == 2:
      a_s,a_p = a_s+1 , a_p+1
    elif diff == 1:
      if s < a_s-a_p:
        a_p +=1
      else:
        a_s +=1
    print a_s,a_p,a_y

if __name__ == '__main__':
  main()
