import sys
result= ["bijective","not a function","surjective","injective","neither injective nor surjective"]
not_func = False
onto = True
one21 = True
r=[]
d=[]
x_used=[]
y_used=[]
def answer(not_func,onto,one21):
    if not_func:
        return result[1]
    elif onto and one21 :
        return result[0]
    elif onto:
        return result[2]
    elif one21:
        return result[3]
    return result[4]

count = 0
for line in sys.stdin:
    if line.split()[0] == "domain":
        d = line.split()[1:]
        x_used = []
    elif line.split()[0] == "codomain":

        if set(r) != set(y_used):
            onto = False
        if count != 0:
            print answer(not_func,onto,one21)
            not_func = False
            onto = True
            one21 = True
        r = line.split()[1:]
        y_used = []
        next(sys.stdin) # don't read the number of mappings
        count +=1
    else:
        x = line.split()[0]
        y = line.split()[-1]
        if x in x_used:
            not_func = True
        x_used.append(x)
        if (not not_func) and (y in y_used):
            one21 = False
        y_used.append(y)

if set(r) != set(y_used):
    onto = False
print answer(not_func,onto,one21)
