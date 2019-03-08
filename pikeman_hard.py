import sys

def main():
  n,t = [int(i) for i in sys.stdin.readline().split()]
  A,B,C,t0 = [int(i) for i in sys.stdin.readline().split()]

  time_count = [0 for i in xrange(C+1)]
  time_count[t0] = 1
  curr, last =  t0, t0
  time_list, time_dict = [t0], {t0:0}
  for i in xrange(1,n):
    curr = ((A*last + B) % C) +1
    if curr in time_dict:
      break
    time_list.append(curr)
    time_dict[curr] = i
    time_count[curr] += 1
    last = curr
  # Now we need to add proper time counts
  rep_start = time_dict[curr]
  reps = len(time_list) - rep_start
  if reps != 0:
    fills_left = n-len(time_list)
    pure_reps = fills_left / reps
    extras = fills_left % reps
    for i in xrange(reps):
      time_count[time_list[i+rep_start]] += pure_reps
      if i < extras:
        time_count[time_list[i+rep_start]] +=1


  penalty,solved = 0,0
  elapsed_time, time = 0,1
  mod = 1000000007
  while time <= C :
    if time_count[time] == 0:
        time += 1
        continue
    remaining_time = t - elapsed_time
    m = min(min(remaining_time/time, time_count[time]), n-solved)
    if m==0 and time_count[time] != 0:
       break
    penalty = (penalty + m*elapsed_time + time*( (m*m+m)/2 )) % mod
    elapsed_time += m*time
    solved += m
    time +=1
  print solved, penalty

if __name__ == '__main__':
  main()
