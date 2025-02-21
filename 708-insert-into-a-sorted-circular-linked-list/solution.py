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

def print_list(head: Optional[Node]):
    arr = []
    curr = head
    while True:
        arr.append(curr.val)
        curr = curr.next
        if curr == head:
            break
    print(arr)

a = Node(1)
b = Node(3)
c = Node(5)

a.next = b
b.next = c
c.next = a

print_list(a)

sol = Solution()
sol.insert(b, 2)

print_list(a)