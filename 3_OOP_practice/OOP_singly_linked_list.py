# 객체지향 구조 연습
# 단순 연결 리스트


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.nodes = []

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f'{self.head}'

    def appends(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.nodes[-1].next = new_node
        self.nodes.append(new_node)

list = SinglyLinkedList()
list.appends(10)
list