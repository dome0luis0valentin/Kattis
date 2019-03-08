import sys

def decode(line):
  pixels = [".", "#"] if line[0] == "." else ["#","."]
  img_row = []
  for i,v in enumerate(line[1:]):
    run = int(v)
    img_row.append(pixels[i%2]*run)
  return "".join(img_row)

def main():
  line = lambda : sys.stdin.readline().strip()
  n = int(line())
  while n != 0:
    image = []
    cols = -1
    invalid = False
    for i in xrange(n):
      img_row = decode(line().split())
      if cols == -1:
        cols = len(img_row)
        image.append(img_row)
      elif cols == len(img_row):
        image.append(img_row)
      else:
        invalid = True
        image.append(img_row)
    print "\n".join(image)
    if invalid:
      print "Error decoding image"
    n = int(line())
    if n!=0:
      print

if __name__ == '__main__':
  main()
