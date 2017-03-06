import sys

def next_collatz(x):
    if x == 1:
        return 1
    if x%2 == 0:
        return x/2
    else:
        return 3*x + 1

def meet(x,y):
    x_seq = {x:0}
    y_seq = {y:0}

    x_step = 0
    y_step = 0
    while not(x in y_seq or y in x_seq):
        if x != 1:
            x = next_collatz(x)
            x_step += 1
            x_seq[x] = x_step
        if y != 1:
            y = next_collatz(y)
            y_step += 1


        y_seq[y] = y_step

    if x in y_seq:
        return x_seq[x],y_seq[x],x
    else:
        return x_seq[y],y_seq[y],y

def main():
    for line in sys.stdin:
        if line.strip() == "0 0":
            return
        x,y = [int(i) for i in line.split()]
        x_step,y_step,meet_val = meet(x,y)
        print x,"needs",x_step, "steps,", y, "needs",y_step,\
              "steps, they meet at",meet_val

if __name__ == '__main__':
    main()
