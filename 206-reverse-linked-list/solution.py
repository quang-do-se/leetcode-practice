from typing import Self, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def generate_from_array(array: list[int], index = 0) -> Self:
        prev_node = None
        head = None

        for e in array:
            node = ListNode(e)
            if prev_node is not None:
                prev_node.next = node
            else:
                head = node

            prev_node = node

        return head

    @staticmethod
    def list_to_array(list: Optional[Self]) -> list[int]:
        array = []
        
        while list is not None:
            array.append(list.val)
            list = list.next

        return array


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive approach
        return self.reverse_list_helper(None, head)

    def reverse_list_helper(self, reversed_list: Optional[ListNode], remaining_list: Optional[ListNode]) -> Optional[ListNode]:
        if remaining_list is None:
            return reversed_list

        node = remaining_list
        remaining_list = remaining_list.next

        node.next = reversed_list

        return self.reverse_list_helper(node, remaining_list)


sol = Solution()
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2,3,4,5]))) == [5,4,3,2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2]))) == [2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([]))) == [])