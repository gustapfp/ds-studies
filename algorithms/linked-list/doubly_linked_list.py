class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.previous_node: "Node | None" = None
        self.next_node: "Node | None" = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    def add_to_front(self, value: int) -> None:
        new_node = Node(value=value)

        if self.head:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def add_to_tail(self, value: int):
        new_node = Node(value=value)
        if self.tail:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_front(self) -> int | None:
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.previous_node = None
        return removed_value

    def remove_from_tail(self) -> int | None:
        if not self.tail:
            return None
        removed_value = self.tail.value

        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous_node
            self.tail.next_node = None

        return removed_value
