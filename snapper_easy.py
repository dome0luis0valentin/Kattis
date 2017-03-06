import sys

next(sys.stdin)#don't need first line
case_num = 1
for line in sys.stdin:
    line = line.strip().split()
    n = int(line[0])
    k = int(line[1])

    min_needed = 2**n -1

    status = "OFF"
    while min_needed < k:
        k = k - min_needed - 1

    if min_needed == k:
        status = "ON"
    print "Case #"+ str(case_num)+":", status
    case_num +=1
