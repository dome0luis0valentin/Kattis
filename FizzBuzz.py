<<<<<<< HEAD
import sys
input_values = sys.stdin.readlines()[0].split()
for i in range(len(input_values)):
    input_values[i] = int (input_values[i])
    
for i in range(1,input_values[2]+1):

    if (i % input_values[0] == 0):
        if (i % input_values[1] == 0):
            print "FizzBuzz"
        else:
            print "Fizz"
    elif (i % input_values[1] == 0):
        print "Buzz"
    else:
        print i
=======
import sys
input_values = sys.stdin.readlines()[0].split()
for i in range(len(input_values)):
    input_values[i] = int (input_values[i])
    
for i in range(1,input_values[2]+1):

    if (i % input_values[0] == 0):
        if (i % input_values[1] == 0):
            print "FizzBuzz"
        else:
            print "Fizz"
    elif (i % input_values[1] == 0):
        print "Buzz"
    else:
        print i
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
