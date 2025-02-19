class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None        

# This solution implements doubly linked list with sentinel nodes
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            node = self.head
            for _ in range(index + 1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - index):
                node = node.prev
        return node.val
        

    def addAtHead(self, val: int) -> None:
        prev, succ = self.head, self.head.next
        self.size += 1
        node = ListNode(val)
        node.prev, node.next = prev, succ
        prev.next, succ.prev = node, node
        return
        

    def addAtTail(self, val: int) -> None:
        prev, succ = self.tail.prev, self.tail
        self.size += 1
        node = ListNode(val)
        node.prev, node.next = prev, succ
        prev.next, succ.prev = node, node
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        
        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            succ = prev.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            prev = succ.prev

        self.size += 1
        node = ListNode(val)   
        node.prev, node.next = prev, succ
        prev.next, succ.prev = node, node
        return        
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            succ = prev.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            prev = succ.prev.prev
        
        self.size -= 1
        prev.next, succ.prev = succ, prev
        return


    def to_array(self) -> None:
        arr = []
        curr = self.head.next
        while curr.next is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def to_array_reverse(self) -> None:
        arr = []
        curr = self.tail.prev
        while curr.prev is not None:
            arr.append(curr.val)
            curr = curr.prev
        return arr

# Your MyLinkedList object will be instantiated and called as such:
my_linked_list = MyLinkedList()

my_linked_list.addAtHead(1)        # 1
print(my_linked_list.to_array() == [1])
print(my_linked_list.to_array_reverse() == [1])

my_linked_list.addAtTail(3)        # 1 -> 3
print(my_linked_list.to_array() == [1, 3])
print(my_linked_list.to_array_reverse() == [1, 3][::-1])

my_linked_list.addAtIndex(0, 2)    # 2 -> 1 -> 3
print(my_linked_list.to_array() == [2, 1, 3])
print(my_linked_list.to_array_reverse() == [2,1,3][::-1])

my_linked_list.addAtIndex(2, 4)    # 2 -> 1 -> 4 -> 3
print(my_linked_list.to_array() == [2, 1, 4, 3])
print(my_linked_list.to_array_reverse() == [2, 1, 4, 3][::-1])

my_linked_list.deleteAtIndex(3)    # 2 -> 1 -> 4
print(my_linked_list.to_array() == [2, 1, 4])
print(my_linked_list.to_array_reverse() == [2, 1, 4][::-1])

my_linked_list.deleteAtIndex(1)    # 2 -> 4
print(my_linked_list.to_array() == [2, 4])
print(my_linked_list.to_array_reverse() == [2, 4][::-1])

my_linked_list.deleteAtIndex(1)    # 2
print(my_linked_list.to_array() == [2])
print(my_linked_list.to_array_reverse() == [2][::-1])

my_linked_list.addAtIndex(1, 1)
print(my_linked_list.to_array() == [2, 1])
print(my_linked_list.to_array_reverse() == [2, 1][::-1])

my_linked_list.deleteAtIndex(0)
print(my_linked_list.to_array() == [1])
print(my_linked_list.to_array_reverse() == [1][::-1])

my_linked_list.addAtTail(3)
print(my_linked_list.to_array() == [1, 3])
print(my_linked_list.to_array_reverse() == [1, 3][::-1])