import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False



sol = Solution()
print(sol.hasCycle(LinkedList.generate_from_array([1,2,3,4,5,6])) == False)