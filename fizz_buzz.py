class Node:
    
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.length = 0

    def append(self,elem):

        cur = self.head
        # self.length+=1

        if(cur.next != None):
            cur = self.tail
            cur = cur.prev
            cur.next = Node(elem)
            this = cur
            cur = cur.next
            cur.prev = cur
            cur.next = self.tail
            self.tail.prev = cur

        else:
            cur.next = Node(elem)
            this = cur
            cur = cur.next
            cur.prev = this
            cur.next = self.tail

            this = cur
            cur = cur.next
            cur.prev = this

        self.length+=1

    def prepend(self,elem):

        cur = self.head

        next_node = cur.next
        cur.next = Node(elem)
        cur = cur.next
        cur.prev = self.head

        cur.next = next_node

        this = cur
        cur = cur.next
        cur.prev = this
        self.length+=1

    def display(self):

        ans = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            ans.append(cur.data)

        return ans
    
    def insertAt(self,elem,number):

        count = 0

        cur = self.head

        while cur.next != None and count<number:
            cur = cur.next
            count+=1

        next_node = cur.next
        cur.next = Node(elem)
        this = cur
        cur = cur.next
        cur.prev = this
        cur.next = next_node
        next_node.prev = cur
        self.length+=1

    def get(self,num):

        count = 0
        cur = self.head

        while cur.next != None and count<num:
            count+=1
            cur = cur.next

        return cur.data
    
    def pop(self,number):

        count = 0

        cur = self.head

        while cur.next != None and count<number:

            count+=1
            cur = cur.next

        if(cur.next != None):
            cur.next = cur.next.next
            this = cur
            cur = cur.next
            cur.prev = this

        else:
            raise ValueError("no")
        
        self.length-=1
    
l1 = doublyLinkedList()

for i in range(0,10):
    l1.append(i)

print(l1.display(),l1.length)

l1.pop(4)

print(l1.display(),l1.length)