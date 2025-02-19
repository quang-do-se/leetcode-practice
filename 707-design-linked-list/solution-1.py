class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# Doubly Linked List
class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if self.head is None or index < 0 or index > self.length - 1:
            return -1

        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node

        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return None

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1

        # Add new node before the current node
        new_node = ListNode(val)
        new_node.prev = curr.prev
        new_node.next = curr
        curr.prev.next = new_node
        curr.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            return None

        if index == 0:
            curr = self.head

            if self.head.next is None:
                self.tail = None
            else:
                self.head.next.prev = None

            self.head = self.head.next
            curr.next = None
            self.length -= 1
            return

        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1

        curr.prev.next = curr.next

        # Handle deleting at the end
        if curr.next is not None:
            curr.next.prev = curr.prev
        else:
            self.tail = self.tail.prev

        curr.next = None
        curr.prev = None
        self.length -= 1


    def to_array(self) -> None:
        arr = []
        curr = self.head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def to_array_reverse(self) -> None:
        arr = []
        curr = self.tail
        while curr is not None:
            arr.append(curr.val)
            curr = curr.prev
        return arr

# Your MyLinkedList object will be instantiated and called as such:
my_linked_list = MyLinkedList()

print(my_linked_list.length == 0)

my_linked_list.addAtHead(1)        # 1
print(my_linked_list.to_array() == [1])
print(my_linked_list.to_array_reverse() == [1])
print(my_linked_list.length == 1)

my_linked_list.addAtTail(3)        # 1 -> 3
print(my_linked_list.to_array() == [1, 3])
print(my_linked_list.to_array_reverse() == [1, 3][::-1])
print(my_linked_list.length == 2)

my_linked_list.addAtIndex(0, 2)    # 2 -> 1 -> 3
print(my_linked_list.to_array() == [2, 1, 3])
print(my_linked_list.to_array_reverse() == [2,1,3][::-1])
print(my_linked_list.length == 3)

my_linked_list.addAtIndex(2, 4)    # 2 -> 1 -> 4 -> 3
print(my_linked_list.to_array() == [2, 1, 4, 3])
print(my_linked_list.to_array_reverse() == [2, 1, 4, 3][::-1])
print(my_linked_list.length == 4)

my_linked_list.deleteAtIndex(3)    # 2 -> 1 -> 4
print(my_linked_list.to_array() == [2, 1, 4])
print(my_linked_list.to_array_reverse() == [2, 1, 4][::-1])
print(my_linked_list.length == 3)

my_linked_list.deleteAtIndex(1)    # 2 -> 4
print(my_linked_list.to_array() == [2, 4])
print(my_linked_list.to_array_reverse() == [2, 4][::-1])
print(my_linked_list.length == 2)

my_linked_list.deleteAtIndex(1)    # 2
print(my_linked_list.to_array() == [2])
print(my_linked_list.to_array_reverse() == [2][::-1])
print(my_linked_list.length == 1)

my_linked_list.addAtIndex(1, 1)
print(my_linked_list.to_array() == [2, 1])
print(my_linked_list.to_array_reverse() == [2, 1][::-1])
print(my_linked_list.length == 2)

my_linked_list.deleteAtIndex(0)
print(my_linked_list.to_array() == [1])
print(my_linked_list.to_array_reverse() == [1][::-1])
print(my_linked_list.length == 1)

my_linked_list.addAtTail(3)
print(my_linked_list.to_array() == [1, 3])
print(my_linked_list.to_array_reverse() == [1, 3][::-1])
print(my_linked_list.length == 2)
