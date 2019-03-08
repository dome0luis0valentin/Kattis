import sys,math

def main():
  t = int(sys.stdin.readline().strip())
  for i in xrange(t):
    r, c = [int(i)+1 for i in sys.stdin.readline().split()]
    col_lvl = int(math.ceil(math.log(c,2)))
    row_lvl = int(math.ceil(math.log(r,2)))

    # correct log  calculation, incase there is floating point/rounding error
    if 2**(col_lvl-1) >= c:
      col_lvl -= 1
    if 2**(row_lvl-1) >= r:
      row_lvl -= 1

    if col_lvl-1 >= row_lvl:
      # Column is doubling
      base = int(2**col_lvl/2)
      ans = base*base + base*(c - base - 1) + r - 1
    else:
      # Row is doubling
      base = int(2**row_lvl/2)
      ans = base*base*2 + (2*base)*(r - base - 1) + c -1
    print ans

if __name__ == '__main__':
  main()
