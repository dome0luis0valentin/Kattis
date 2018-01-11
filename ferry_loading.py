import sys

class Node:
    def __init__(self,key):
        self.next = None
        self.data = key

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self,key):
        n = Node(key)
        if (self.head == None):
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
    def pop(self):
        if (self.head == None):
            return None,None
        n = self.head
        self.head = self.head.next
        return n.data
    def peak(self):
        if (self.head == None):
            return None,None
        return self.head.data
    def isEmpty(self):
        return self.head == None

    def __repr__(self):
        n = self.head
        str_r = []
        while(n!=None):
            str_r.append(str(n.data))
            n = n.next
        return " ".join(str_r)

def process(q,t,max_load):
    res = {}
    left,right = 0,1
    curr_t,side = 0,left
    while(True):
        side_min,c_id = q[side].peak()
        loaded = 0
        while(side_min!=None and side_min <= curr_t and loaded < max_load):
            loaded+=1
            res[c_id] = curr_t+t
            q[side].pop()
            side_min,c_id = q[side].peak()
        if (loaded!=0):
            curr_t += t
            side = left if side==right else right
        elif (not q[left].isEmpty() and not q[right].isEmpty()):
            if q[left].peak()[0] < q[right].peak()[0]:
                if side == left: # wait
                    curr_t = q[left].peak()[0]
                else: # switch sides right when a car arrives at the other side
                    arr_t = q[left].peak()[0]
                    if curr_t >= arr_t:
                        curr_t += t
                    else:
                        curr_t = arr_t + t
                    side = left
            elif q[left].peak()[0] == q[right].peak()[0]: #just wait where you are
                curr_t = q[side].peak()
            else:
                if side==left:# switch sides when car arrives at the other side
                    arr_t = q[right].peak()[0]
                    if curr_t >= arr_t:
                        curr_t += t
                    else:
                        curr_t = arr_t + t
                    side = right
                else: # wait
                    curr_t = q[right].peak()[0]
        else:
            curr_t += t
            break
    # only one side is left
    qr = q[right] if q[left].isEmpty() else q[left]

    while(not qr.isEmpty()):
        side_min,c_id = qr.peak()
        loaded = 0
        while(side_min!=None and side_min<=curr_t and loaded< max_load):
            loaded+=1
            res[c_id] = curr_t+t
            qr.pop()
            side_min,c_id = qr.peak()
        if loaded != 0:
            curr_t += t
            if (not qr.isEmpty()):
                next_min = qr.peak()[0]
                if next_min >= curr_t:
                    curr_t = next_min+t
                else:
                    curr_t += t # come back immediately
        else:
            curr_t = qr.peak()[0] # just wait

    return res

def main():
    cases = int(sys.stdin.readline().strip())
    for c in xrange(cases):
        n,t,m = [int(i) for i in sys.stdin.readline().split()]
        left,right = Queue(),Queue()
        for car in xrange(m):
            time,side = sys.stdin.readline().split()
            if side == 'left':
                left.push((int(time),car))
            else:
                right.push((int(time),car))
        res = process([left,right],t,n)
        for c in xrange(m):
            print res[c]
        print

if __name__ == '__main__':
    main()
