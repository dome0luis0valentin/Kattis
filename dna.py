import sys

def solve(profile, start):
  steps = 0
  while len(profile) > 0:
    if start == "A" and len(profile) % 2 == 1:
      profile.pop()
    elif start == "A" and len(profile)  % 2 == 0:
      n = profile.pop()
      steps += 1
      if n > 1:
        start = "B"
    elif start == "B" and len(profile) % 2 == 0:
      profile.pop()
    else:
      n = profile.pop()
      steps += 1
      if n > 1:
        start = "A"
  return steps

def main():
  n = int(sys.stdin.readline().strip())
  profile = []
  line = sys.stdin.readline().strip()
  start = line[0]
  last, c = start, 0
  for i in line:
    if i == last:
      c +=1
    else:
      profile.append(c)
      c = 1
      last = i
  profile.append(c)
  print solve(profile, start)

if __name__ == '__main__':
  main()
