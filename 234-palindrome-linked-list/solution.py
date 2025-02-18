from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        curr = head
        while curr is not None:
            array.append(curr.val)
            curr = curr.next

        i = 0
        j = len(array) -1
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1
        return True



sol = Solution()
print(sol.isPalindrome(LinkedList.generate_from_array([1,2,2,1])))
print(sol.isPalindrome(LinkedList.generate_from_array([1,2,2,3])))