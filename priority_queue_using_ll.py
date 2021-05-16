class Node:
    # each node will contains --  data, priority and address of next node
    def __init__(self, data, priority):
        self.data = data 
        self.next = None 
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.head = None 

    def insert(self, val, prt):
        ''' function to insert value and priority
            Time complexity - O(1)
        '''
        node = Node(val, prt)
        if self.head is None:
            # if head is null then point head and temp to node
            self.head = node 
            self.temp = node 
        else:
            # else point next of temp to node and assign node to temp
            self.temp.next = node 
            self.temp = node 

    def delete(self):
        '''
           function to delete value according to priority
           Time complexity - O(n)
        '''
        if self.head is not None:
            prev = self.head 
            temp = self.head 
            max = self.head 
            while temp.next:
                if temp.next.priority > max.priority:
                    max = temp.next 
                    prev = temp 
                temp = temp.next 
            if max == self.head:
                self.head = max.next
            else:        
                prev.next = max.next 
            print('Dequeued:', max.data)
        else:
            print('Queue is empty')

    def traverse(self):
        temp = self.head 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()            


q = PriorityQueue()
q.insert(45, 4)
q.insert(56, 15)
q.insert(21, 1)
q.insert(12, 8) 
q.insert(89, 7)
q.insert(57, 0)
q.traverse()
q.delete()
q.delete()
q.delete()
q.delete()
q.delete()
q.delete()
q.delete()