import sys, math

def main():
  history = sys.stdin.readline().strip()
  rank, stars = 25, 0
  inrow_wins = 0
  rank_stars = { 5: 2, 4: 3, 3:4, 2:5, 1:5 }
  for g in history:
    if rank == 0:
      break
    if g == "W":
      inrow_wins += 1
      stars += 1
      if inrow_wins >= 3 and 6 <= rank <=25:
        stars +=1
      r = int(math.ceil(rank/5.0))
      if stars > rank_stars[r]:
        stars -= rank_stars[r]
        rank -= 1
    elif g == "L":
      inrow_wins = 0
      if 1 <= rank < 20:
        stars -= 1
        if stars < 0 :
          rank += 1
          r = int(math.ceil(rank/5.0))
          stars = rank_stars[r] - 1
      elif rank == 20 and stars > 0:
        stars -= 1
  print "Legend" if rank == 0 else rank


if __name__ == '__main__':
  main()

