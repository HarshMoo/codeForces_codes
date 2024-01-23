class Node:

    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = Node()

    def append(self,elem):

        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = Node(elem)

    def display(self):
        ans = []

        cur = self.head

        while cur.next != None:
            cur = cur.next

            ans.append(cur.data)

        return ans