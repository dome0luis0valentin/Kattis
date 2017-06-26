import sys
import bisect
import math

counter = 0
request = []

for line in sys.stdin:

    if counter == 0:
        capacity = int(line.strip().split()[-1]) # can handle per sec
        counter = 1
    else:
        request.append(int(line.strip()))

total_time = (request[-1]/1000) + 2


initial = 0
final = 0
max_req_perSec = 0
for i in range(total_time):
    final = bisect.bisect(request,1000*i-1)
    num = len(request[initial:final])
    if num > max_req_perSec:
        max_req_perSec = num
    initial = final
print int(math.ceil(max_req_perSec / (capacity*1.0)))
