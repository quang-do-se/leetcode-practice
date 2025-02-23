from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        k %= size
        if k == 0:
            return head
        
        fast = head
        while k > 0:
            fast = fast.next
            k -= 1

        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
    

sol = Solution()
print(LinkedList.list_to_array(sol.rotateRight(LinkedList.generate_from_array([1,2,3,4,5]), 5)) == [1,2,3,4,5])
print(LinkedList.list_to_array(sol.rotateRight(LinkedList.generate_from_array([1,2,3,4,5]), 0)) == [1,2,3,4,5])
print(LinkedList.list_to_array(sol.rotateRight(LinkedList.generate_from_array([1,2,3,4,5]), 1)) == [5,1,2,3,4])
print(LinkedList.list_to_array(sol.rotateRight(LinkedList.generate_from_array([1,2,3,4,5]), 2)) == [4,5,1,2,3])
print(LinkedList.list_to_array(sol.rotateRight(LinkedList.generate_from_array([1,2,3,4,5]), 3)) == [3,4,5,1,2])
print(LinkedList.list_to_array(sol.rotateRight(LinkedList.generate_from_array([1,2,3,4,5]), 4)) == [2,3,4,5,1])