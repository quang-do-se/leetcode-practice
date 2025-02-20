from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

# Recursive approach
class Solution:
    def get_length(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def add_helper(self, l1: Optional[ListNode], l2: Optional[ListNode])  -> (Optional[ListNode], int):
        if not l1:  # Base case: end of both lists
            return None, 0

        next_node, carry = self.add_helper(l1.next, l2.next)  # Recur on next digits

        sum_val = l1.val + l2.val + carry
        carry, digit = divmod(sum_val, 10)

        current_node = ListNode(digit)
        current_node.next = next_node

        return current_node, carry

    def add_remaining(self, l1: Optional[ListNode], stop_node: Optional[ListNode], result: Optional[ListNode], carry: int) -> (Optional[ListNode], int):
        """ Adds remaining digits from the longer list before reaching stop_node. """
        if l1 == stop_node:
            return result, carry  # Stop recursion here

        next_node, carry = self.add_remaining(l1.next, stop_node, result, carry)

        sum_val = l1.val + carry
        carry, digit = divmod(sum_val, 10)

        current_node = ListNode(digit)
        current_node.next = next_node

        return current_node, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = self.get_length(l1), self.get_length(l2)

        # Ensure l1 is the longer list (swap if needed)
        if len1 < len2:
            l1, l2 = l2, l1
            len1, len2 = len2, len1

        diff = len1 - len2
        longer_head = l1
        for _ in range(diff):
            longer_head = longer_head.next  # Move pointer to where lists align

        # Add aligned parts recursively
        aligned_result, carry = self.add_helper(longer_head, l2)

        # Add carry to the unmatched part of the longer list
        longer_result, carry = self.add_remaining(l1, longer_head, aligned_result, carry)

        # If there's a leftover carry, create a new head node
        if carry:
            new_node = ListNode(carry)
            new_node.next = longer_result
            aligned_result = new_node

        return aligned_result


sol = Solution()
print(LinkedList.list_to_array(sol.addTwoNumbers(LinkedList.generate_from_array([3,4,2]), LinkedList.generate_from_array([4,6,5]))))
print(LinkedList.list_to_array(sol.addTwoNumbers(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([9, 9, 9]))))
print(LinkedList.list_to_array(sol.addTwoNumbers(LinkedList.generate_from_array([0]), LinkedList.generate_from_array([0]))))