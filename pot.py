<<<<<<< HEAD
import sys
next(sys.stdin)
total = 0
for i in sys.stdin:
    i=i.strip()
    if i.isdigit():
        total += int(i[:-1]) ** int(i[-1])

print total
=======
import sys
next(sys.stdin)
total = 0
for i in sys.stdin:
    i=i.strip()
    if i.isdigit():
        total += int(i[:-1]) ** int(i[-1])

print total
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
