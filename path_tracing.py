import sys

def main():
  x, y = 0, 0
  dx, dy = [x], [y]
  d = set()

  for line in sys.stdin.readlines():
    command = line.strip()
    if command == 'down':
      y += 1
    elif command == 'left':
      x -= 1
    elif command == 'up':
      y -= 1
    else:
      x += 1
    dx.append(x)
    dy.append(y)
    d.add((x,y))

  left, right = min(dx), max(dx)
  top, bottom = min(dy), max(dy)

  print '#' * (right-left + 3)
  for y in xrange(top, bottom+1):
    row = ['#']
    for x in xrange(left, right+1):
      if x == 0 and y == 0:
        row.append('S')
      elif x == dx[-1] and y == dy[-1]:
        row.append('E')
      elif (x,y) in d:
        row.append('*')
      else:
        row.append(' ')
    row.append('#')
    print ''.join(row)
  print '#' * (right-left + 3)

if __name__ == '__main__':
  main()
