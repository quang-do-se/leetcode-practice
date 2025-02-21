# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)

        if head is None:
            newNode.next = newNode
            return newNode

        p = head
        c = head.next
        while c != head:
            if not c.val >= p.val:
                break
            p = c
            c = c.next

        smallest = c

        while insertVal > c.val:
            p = c
            c = c.next
            if c == smallest:
                break

        p.next = newNode
        newNode.next = c
        return head

def get_list(head: Optional[Node]):
    arr = []
    curr = head
    while True:
        arr.append(curr.val)
        curr = curr.next
        if curr == head:
            break
    return arr


a = Node(1)
b = Node(3)
c = Node(3)
d = Node(5)

sol = Solution()

a.next = b
b.next = c
c.next = d
d.next = a
sol.insert(b, 2)
print(get_list(a) == [1,2,3,3,5])

a.next = b
b.next = c
c.next = d
d.next = a
sol.insert(b, 1)
print(get_list(a) == [1,3,3,5,1])

a.next = b
b.next = c
c.next = d
d.next = a
sol.insert(b, 4)
print(get_list(a) == [1,3,3,4,5])

a.next = b
b.next = c
c.next = d
d.next = a
sol.insert(b, 5)
print(get_list(a) == [1,3,3,5,5])

a.next = b
b.next = c
c.next = d
d.next = a
sol.insert(b, 0)
print(get_list(a) == [1,3,3,5,0])