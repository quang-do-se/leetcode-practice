from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev = sentinel
        curr = head

        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                temp = curr
                curr = curr.next
                temp.next = None
            else:
                prev = curr
                curr = curr.next

        return sentinel.next
                


sol = Solution()
print(LinkedList.list_to_array(sol.removeElements(LinkedList.generate_from_array([1,2,3,4,5]), 1)) == [2,3,4,5])
print(LinkedList.list_to_array(sol.removeElements(LinkedList.generate_from_array([1,2,3,4,5]), 3)) == [1,2,4,5])
print(LinkedList.list_to_array(sol.removeElements(LinkedList.generate_from_array([1]), 1)) == [])
print(LinkedList.list_to_array(sol.removeElements(LinkedList.generate_from_array([]), 1)) == [])
print(LinkedList.list_to_array(sol.removeElements(LinkedList.generate_from_array([1,2,3,4,5]), 5)) == [1,2,3,4])