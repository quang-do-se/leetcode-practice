from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        index = 2
        curr = head.next
        last_odd = head         # last node in ordered ODD group
        last_even = head.next   # last node in ordered EVEN group

        while curr is not None:
            if index % 2 == 1:
                last_even.next = curr.next
                curr.next = last_odd.next
                last_odd.next = curr

                # Move curr forward and update odd group
                curr = last_even.next
                last_odd = last_odd.next
            else:
                last_even = curr
                curr = curr.next
            index += 1

        return head


sol = Solution()
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([1,2,3,4]))) == [1, 3, 2, 4])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([1,2,3,4,5]))) == [1, 3, 5, 2, 4])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([1,2,3,4,5,6,7]))) == [1, 3, 5, 7, 2, 4, 6])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([1,2,3,4,5]))) == [1, 3, 5, 2, 4])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([1,2]))) == [1, 2])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([1]))) == [1])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([]))) == [])
print(LinkedList.list_to_array(sol.oddEvenList(LinkedList.generate_from_array([2,1,3,5,6,4,7]))) == [2, 3, 6, 7, 1, 5, 4])