<<<<<<< HEAD
import sys

inital_values = sys.stdin.read().split()

prime_regis = [2,3,5,7,11,13,17,19]
for i in range(len(inital_values)):
    inital_values[i] = int(inital_values[i])

ops = 0
blowup = False

while not blowup:
    current = 0
    while current < 8:
        if inital_values[current] < prime_regis[current]-1:
            inital_values[current] = inital_values[current] + 1
            ops +=1
            break
        else:
            if  current == 7:
                blowup = True
                current +=1
            else:
                inital_values[current] = 0
                current +=1

print ops
=======
import sys

inital_values = sys.stdin.read().split()

prime_regis = [2,3,5,7,11,13,17,19]
for i in range(len(inital_values)):
    inital_values[i] = int(inital_values[i])

ops = 0
blowup = False

while not blowup:
    current = 0
    while current < 8:
        if inital_values[current] < prime_regis[current]-1:
            inital_values[current] = inital_values[current] + 1
            ops +=1
            break
        else:
            if  current == 7:
                blowup = True
                current +=1
            else:
                inital_values[current] = 0
                current +=1

print ops
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
