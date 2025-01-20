from typing import List, Self, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def generate_from_array(array: List[int], index = 0) -> Self:
        if not array:
            return None

        head = ListNode(array[0])
        current = head

        for e in array[1:]:
            current.next = ListNode(e)
            current = current.next

        return head

    @staticmethod
    def list_to_array(input_list: Optional[Self]) -> List[int]:
        array = []

        while input_list is not None:
            array.append(input_list.val)
            input_list = input_list.next

        return array


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Interative approach
        reversed_list = None

        while head is not None:
            next_head = head.next
            head.next = reversed_list
            reversed_list = head
            head = next_head

        return reversed_list


sol = Solution()
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2,3,4,5]))) == [5,4,3,2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2]))) == [2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([]))) == [])