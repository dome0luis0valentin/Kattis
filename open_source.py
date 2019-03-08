import sys
from collections import defaultdict

def process(proj_map):
  pairs = [(-1*len(proj_map[i]),i) for i in proj_map]
  pairs.sort()
  for l,p in pairs:
    print p, -1*l

def main():
  proj_name = ""
  proj_map  = {}
  name_proj = defaultdict(set)
  forbidden_names = set()
  for line in sys.stdin:
    line = line.strip()
    if line.isupper():
      proj_name = line
      proj_map[proj_name] = set()
    elif line == "1":
      process(proj_map)
      proj_map, proj_name, name_proj = {}, "", defaultdict(set)
    elif line == "0":
      return
    else:
      name_proj[line].add(proj_name)
      if len(name_proj[line]) == 1:
        proj_map[proj_name].add(line)
      else:
        for p in proj_map:
          if line in proj_map[p]:
            proj_map[p].remove(line)

if __name__ == '__main__':
  main()

