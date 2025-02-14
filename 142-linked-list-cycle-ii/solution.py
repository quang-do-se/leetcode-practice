import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if head is None:
            return None

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None