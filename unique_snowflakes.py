import sys

def main():
  t = int(sys.stdin.readline().strip())
  for i in xrange(t):
    n = int(sys.stdin.readline().strip())
    index_map = {}
    max_sofar = 0
    curr_start = 0
    for j in xrange(n):
      flake = int(sys.stdin.readline().strip())
      if flake in index_map:
        last_seen = index_map[flake]
        if last_seen < curr_start:
          index_map[flake] = j
        else:
          len_sofar = j-curr_start
          if max_sofar < len_sofar:
            max_sofar = len_sofar
          curr_start = last_seen + 1
      index_map[flake] = j

    curr_len = n-curr_start
    if max_sofar < curr_len:
      print curr_len
    else:
      print max_sofar

if __name__ == '__main__':
  main()
