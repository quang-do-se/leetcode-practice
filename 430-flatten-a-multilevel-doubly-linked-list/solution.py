
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        curr = head

        while curr is not None:
            if curr.child:
                sub_list = self.flatten(curr.child)

                next = curr.next
                curr.next = sub_list
                sub_list.prev = curr

                tail_of_sub_list = sub_list
                while tail_of_sub_list is not None and tail_of_sub_list.next is not None:
                    tail_of_sub_list = tail_of_sub_list.next

                tail_of_sub_list.next = next

                if next:
                    next.prev = tail_of_sub_list

                curr.child = None
                curr = next
            else:
                curr = curr.next

        return head