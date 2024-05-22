from typing import Union

from requests import head


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Union[Node, None] = None


class LinkedList:
    def __init__(self, head: Union[int, None] = None) -> None:
        self.head: Union[Node, None] = None if head == None else Node(head)

    def isEmpty(self) -> bool:
        return self.head == None

    def getLength(self) -> int:
        size: int = 0
        current: Union[Node, None] = self.head
        while current:
            current = current.next
            size += 1
        return size

    # Insert

    def insert_at_begining(self, data: int) -> None:
        node: Node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data: int) -> None:
        node: Node = Node(data)
        if not self.head:
            self.head = node
            return
        current: Node = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_at_index(self, data: int, index: int) -> None:
        if index < 0:
            print("[E]: index must be >= 0")

        current_index: int = 0
        current_node: Union[Node, None] = self.head
        node: Node = Node(data)

        if index == current_index:
            self.insert_at_begining(data)
            return

        while current_node and current_index + 1 < index:
            current_index += 1
            current_node = current_node.next

        if current_node:
            node.next = current_node.next
            current_node.next = node

            return

        print(f"invalid index: {index}")

    # Delete
    def delete_first(self) -> None:
        if not self.head:
            print("linked ist is empty")
            return
        self.head = self.head.next

    def delete_last(self) -> None:

        if not self.head:
            print("linked ist is empty")
            return
        if not self.head.next:
            self.head = None
            return

        current: Node = self.head
        while current.next:
            if not current.next.next:
                break
            current = current.next

        current.next = None

    def delete_at_index(self, index) -> None:
        if not self.head:
            print("linked list is empty")
            return

        current_index: int = 0
        if index == current_index:
            self.delete_first()
            return

        current_node: Union[Node, None] = self.head
        while current_node and current_index + 1 < index:
            current_index += 1
            current_node = current_node.next

        if current_node:
            current_node.next = current_node.next.next if current_node.next else None

            return

        print(f"invalid index: {index}")

    def __head(self, node: Node) -> None:
        self.head = node

    def __str__(self) -> str:
        string: str = ""
        current: Union[Node, None] = self.head
        while current:
            string += f"{current.data}"
            current = current.next
            if current:
                string += " -> "

        return string

    @classmethod
    def from_node(cls, node: Node):
        linked_list: LinkedList = LinkedList()
        linked_list.__head(node)
        return linked_list


if __name__ == "__main__":
    node = Node(5)
    node.next = Node(6)
    node.next.next = Node(7)
    node.next.next.next = Node(8)

    print(node.data)
    print(node.next.data)
    print(node.next.next.data)
    print(node.next.next.next.data)

    linked_list: LinkedList = LinkedList.from_node(node)
    linked_list2: LinkedList = LinkedList()
    print(linked_list)

    print(linked_list2.isEmpty())
    linked_list2.insert_at_end(0)
    linked_list2.insert_at_end(2)
    linked_list2.insert_at_end(7)
    print(linked_list2)
    linked_list2.insert_at_begining(4)
    print(linked_list2)
    linked_list2.insert_at_index(1, 2)
    print(linked_list2)
    linked_list2.delete_first()
    print(linked_list2)
    linked_list2.delete_last()
    linked_list2.delete_last()
    # linked_list2.delete_last()
    # linked_list2.delete_last()
    print(linked_list2)

    linked_list2.delete_at_index(3)
    print(linked_list2)
    linked_list3: LinkedList = LinkedList()
    print("length", linked_list3.getLength())
