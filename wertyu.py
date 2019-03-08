import sys

words = "`1234567890-= QWERTYUIOP[]\\ ASDFGHJKL;' ZXCVBNM,./"

def mkConversion(row):
  cov = {}
  for i in xrange(len(row)-1):
    cov[row[i+1]] = row[i]
  cov[" "] = " "
  return cov

def main():
  conversion = mkConversion(words)

  for line in sys.stdin:
    l = []
    for ch in line.strip():
      l.append(conversion[ch])
    print "".join(l)

if __name__ == '__main__'
