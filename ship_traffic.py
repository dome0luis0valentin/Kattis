import sys

# use python3 for better floating point calculation

def comb(curr, nxt):
  i,j = 0, 0
  final = []
  while (i < len(curr) and j < len(nxt)):
    s1,e1 = curr[i]
    s2,e2 = nxt[j]
    s,e = max(s1,s2), min(e1,e2)
    if s < e:
      final.append((s,e))
    if e1 > e2:
      j += 1
    elif e2 > e1:
      i+=1
    else:
      i,j = i+1, j+1
  return final

def multi(intervals):
  n = len(intervals)
  if n == 1:
    return intervals[0]
  if n % 2 == 0:
    f_h, s_h = intervals[:n//2], intervals[n//2:]
    sol1, sol2 = multi(f_h), multi(s_h)
  else:
    sol1, sol2 = intervals[0], multi(intervals[1:])
  return comb(sol1, sol2)

def main():
  line = lambda : sys.stdin.readline().split()
  n, width, ship_s, ferry_v, t0, t1 = map(int, line())
  ferry_lane_crossing = float(width)/ferry_v
  occupied = []
  for i in range(n):
    l = line()
    direction = l[0]
    ship_v = ship_s*(1.0 if direction == "E" else -1.0)
    ships = int(l[1])
    max_k = 2*ships

    delta = ferry_lane_crossing*i
    k = 2
    lane_occupied = []
    while (k <= max_k):
      length, pos = int(l[k]), int(l[k+1])
      start_time = (0-pos)/ship_v
      end_time = start_time + (length/ship_s)
      lane_occupied.append((start_time, end_time))
      k +=2
    if direction == "E":
      occupied.append(reversed(lane_occupied))
    else:
      occupied.append(lane_occupied)

  free = [[(t0,t1)]]
  for i in range(n):
    invalid_times = occupied[i]
    delta = ferry_lane_crossing*i
    curr_t = delta
    f = []
    for s,e in invalid_times:
      last_start = s - ferry_lane_crossing
      if last_start > curr_t:
        f.append((curr_t-delta, last_start-delta))
      curr_t = e
      if curr_t > t1 + delta:
        break
    if curr_t < t1+delta:
      f.append((curr_t-delta, t1))
    free.append(f)

  print (max(map(lambda x:x[1]-x[0], multi(free))))

if __name__ == '__main__':
  main()
