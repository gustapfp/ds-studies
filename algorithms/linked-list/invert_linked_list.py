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
