from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev = None
        curr = head

        while curr is not None:
            if curr.val == val:
                if prev is None:   # Remove beginning
                    temp = head
                    head = head.next
                    temp.next = None
                    curr = head
                else:   # Remove middle and end
                    prev.next = curr.next
                    temp = curr
                    curr = curr.next
                    temp.next = None
            else:
                prev = curr
                curr = curr.next

        return head
                



sol = Solution()
print(LinkedList.list_to_array(sol.removeElements(LinkedList.generate_from_array([1,2,3,4,5]), 1)))