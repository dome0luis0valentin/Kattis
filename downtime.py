import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self,data):
        self.count += 1
        a_node = Node(data)
        if self.head == None:
            self.head = a_node
            self.tail = a_node
        else:
            self.tail.next = a_node
            a_node.prev = self.tail
            self.tail = a_node

    def peek(self):
        return self.head.data if self.head!=None else None

    def pop(self):
        self.count -=1
        if self.head != None:
            val = self.head.data
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            return val
        else:
            return None

    def __repr__(self):
        # expensive method - should use only for debug
        rep_str = []
        curr_node = self.head
        while(curr_node != None):
            rep_str.append(str(curr_node.data))
            curr_node = curr_node.next
        return " ".join(rep_str)

def main():

    n,capacity = [int(i) for i in sys.stdin.readline().split()]
    thread_count = 0
    active_threads = DoublyLinked()

    for i in xrange(n):
        request = int(sys.stdin.readline().strip())
        if active_threads.count == thread_count:
            if active_threads.count!=0 and active_threads.peek()+1000<=request:
                active_threads.pop()
                active_threads.push(request)
            else:
                thread_count += 1
                active_threads.push(request)
        else:
            active_threads.push(request)

    if thread_count % capacity == 0:
        print thread_count/capacity
    else:
        print thread_count/capacity + 1


if __name__ == '__main__':
    main()
