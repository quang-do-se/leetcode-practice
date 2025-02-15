import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr_a = headA
        len_a = 0
        while curr_a != None:
            curr_a = curr_a.next
            len_a += 1

        curr_b = headB
        len_b = 0
        while curr_b != None:
            curr_b = curr_b.next
            len_b += 1

        if len_a > len_b:
            longer_curr = headA
            shorter_curr = headB
            diff_len = len_a - len_b
        else:
            longer_curr = headB
            shorter_curr = headA
            diff_len = len_b - len_a

        i = 0
        while i < diff_len and longer_curr is not None:
            longer_curr = longer_curr.next
            i += 1

        while longer_curr is not None:
            if longer_curr == shorter_curr:
                return longer_curr
            longer_curr = longer_curr.next
            shorter_curr = shorter_curr.next

        return None