# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Loop through original list
# Create copies of the original nodes with next pointers
# Store a map of original nodes -> clone nodes

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        clone_map = {}

        curr = head

        prev_clone = None
        curr_clone = Node(0)
        clone_head = curr_clone

        while curr:
            prev_clone = curr_clone
            curr_clone = clone_map.get(curr, None)

            if not curr_clone:
                curr_clone = Node(curr.val)
                clone_map[curr] = curr_clone

            prev_clone.next = curr_clone

            if curr.random:
                random_clone = clone_map.get(curr.random, None)
                if not random_clone:
                    random_clone = Node(curr.random.val)
                    clone_map[curr.random] = random_clone

                curr_clone.random = random_clone
                
            curr = curr.next
            
        return clone_head.next


a = Node(1)

map = {}
map[a] = None

print(map)