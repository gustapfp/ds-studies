from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListOperations:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt_pointer = head
        while nxt_pointer and nxt_pointer.next:
            nxt_pointer = nxt_pointer.next.next
            head = head.next()

        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()

        while list1 and list2:
            if list2.val > list1.val:
                head.next = list1
                list1, head = list1.next, list1
            else:
                head.next = list2
                list2, head = list2.next, list2
        if list1 or list2:
            head.next = list1 if list1 else list2
        return dummy.next
