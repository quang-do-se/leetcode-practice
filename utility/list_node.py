from typing import List, Optional, Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
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
