import sys
import math

area = int(sys.stdin.readlines()[0].strip())
print '{0:.16f}'.format(math.sqrt(area) * 4.0)
