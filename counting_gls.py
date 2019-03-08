import sys

def count_gls(gls, seq, sofar = 0):
  if len(gls) == 0:
    return sofar
  count = 0
  for i in seq:
    if i<gls[0]:
      count += 1
  return count_gls(gls[1:], seq, sofar+count)

def count_gls(gls,seq):
  total = 0
  while len(gls) > 1:
    start_gls = gls[0]
    for i in seq:

