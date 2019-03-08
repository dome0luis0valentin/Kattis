import sys
from collections import defaultdict

def solve(graph, start, end):
  fq,bq = set([start]),set([end])
  nxt = set()
  steps = 0
  seenf, seenb = set(), set()
  while len(fq)+len(bq) > 0:
    # forward steps
    while len(fq) > 0:
      node = fq.pop()
      seenf.add(node)
      if node in bq:
        return steps
      for v in graph[node]:
        if v not in seenf:
          nxt.add(v)
    steps +=1
    fq, nxt = nxt, set()
    # backward steps
    while len(bq) > 0:
      node = bq.pop()
      seenb.add(node)
      if node in fq:
        return steps
      for v in graph[node]:
        if v not in seenb:
          nxt.add(v)
    steps +=1
    bq, nxt = nxt, set()

  return -1

def main():
  restart = True
  for line in sys.stdin:
    if restart:
      cl,cr = 0,0
      graph = defaultdict(list)
      l,r,c = map(int, line.split())
      prev_lvl = ["#"*c for i in xrange(r)]
      prev_row = "#"*c
      curr_lvl = []
      restart= False
      start, end = (0,0,0), (0,0,0)
      continue
    line = line.strip()
    for cc,i in enumerate(line):
      if i == "S":
        start = (cl,cr,cc)
      elif i == "E":
        end = (cl,cr,cc)
      elif i == "#":
        continue

      # check up
      if prev_lvl[cr][cc] != "#":
        graph[(cl,cr,cc)].append((cl-1,cr,cc))
        graph[(cl-1,cr,cc)].append((cl,cr,cc))
      # check left
      if cc != 0 and line[cc-1] != "#":
        graph[(cl,cr,cc)].append((cl,cr,cc-1))
        graph[(cl,cr,cc-1)].append((cl,cr,cc))
      # check north
      if prev_row[cc] != "#":
        graph[(cl,cr,cc)].append((cl,cr-1,cc))
        graph[(cl,cr-1,cc)].append((cl,cr,cc))

    cr += 1
    if line == "":
      cl += 1
      cr = 0
      prev_row = "#"*c
      prev_lvl, curr_lvl = curr_lvl, []
    else:
      prev_row = line
      curr_lvl.append(line)

    if cl == l:
      restart = True
      steps = solve(graph, start, end)
      if steps == -1:
        print "Trapped!"
      else:
        print "Escaped in {} minute(s).".format(steps)

if __name__ == '__main__':
  main()
