from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev



sol = Solution()
print(LinkedList.list_to_array(sol.reverseList(LinkedList.generate_from_array([1,2,3,4,5]))))
print(LinkedList.list_to_array(sol.reverseList(LinkedList.generate_from_array([1,2,3,4,5]))) == [5,4,3,2,1])
print(LinkedList.list_to_array(sol.reverseList(LinkedList.generate_from_array([1,2]))) == [2,1])
print(LinkedList.list_to_array(sol.reverseList(LinkedList.generate_from_array([]))) == [])