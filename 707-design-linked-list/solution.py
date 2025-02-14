class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None or index < 0 or index >= self.length:
            return -1
        
        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1

        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        
        prev = None
        curr = self.head
        while curr is not None:
            prev = curr
            curr = curr.next
        
        prev.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return None
        
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        
        i = 0
        prev = None
        curr = self.head
        while i < index:
            prev = curr
            curr = curr.next
            i += 1
        
        new_node.next = curr
        prev.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            return None
        
        if index == 0:
            curr = self.head
            self.head = self.head.next
            curr.next = None
            self.length -= 1
            return
        
        i = 0
        prev = None
        curr = self.head
        while i < index:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        curr.next = None
        self.length -= 1


    def to_array(self) -> None:
        arr = []
        curr = self.head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr

# Your MyLinkedList object will be instantiated and called as such:
my_linked_list = MyLinkedList()
print(my_linked_list.length == 0)

my_linked_list.addAtHead(1)        # 1
print(my_linked_list.length == 1)

my_linked_list.addAtTail(3)        # 1 -> 3
print(my_linked_list.length == 2)

my_linked_list.addAtIndex(0, 2)    # 2 -> 1 -> 3
print(my_linked_list.to_array() == [2, 1, 3])
print(my_linked_list.length == 3)

my_linked_list.addAtIndex(2, 4)    # 2 -> 1 -> 4 -> 3
print(my_linked_list.to_array() == [2, 1, 4, 3])
print(my_linked_list.length == 4)

my_linked_list.deleteAtIndex(1)    # 2 -> 4 -> 3
print(my_linked_list.length == 3)

my_linked_list.deleteAtIndex(0)    # 4 -> 3
print(my_linked_list.length == 2)

my_linked_list.deleteAtIndex(0)
print(my_linked_list.length == 1)

my_linked_list.deleteAtIndex(0)
print(my_linked_list.length == 0)

my_linked_list.addAtTail(1)
print(my_linked_list.length == 1)