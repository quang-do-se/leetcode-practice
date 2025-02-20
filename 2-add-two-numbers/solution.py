from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2

        sum_list = ListNode(0)
        tail = sum_list

        carry = 0
        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            r = v1 + v2 + carry
            
            carry = 0
            if r >= 10:
                carry = 1
                r -= 10
            
            tail.next = ListNode(r)
            tail = tail.next

            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        return sum_list.next


sol = Solution()
print(LinkedList.list_to_array(sol.addTwoNumbers(LinkedList.generate_from_array([2,4,3]), LinkedList.generate_from_array([5,6,4]))) == [7, 0, 8])
print(LinkedList.list_to_array(sol.addTwoNumbers(LinkedList.generate_from_array([9,9,9,9,9,9,9]), LinkedList.generate_from_array([9,9,9,9]))) == [8,9,9,9,0,0,0,1])
print(LinkedList.list_to_array(sol.addTwoNumbers(LinkedList.generate_from_array([0]), LinkedList.generate_from_array([0]))) == [0])