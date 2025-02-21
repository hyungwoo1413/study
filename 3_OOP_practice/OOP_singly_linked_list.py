# 객체지향 구조 연습
# 단순 연결 리스트




class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.nodes = []

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def node_append(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            self.nodes = self.data
            self.head.next = self.data
                
        

list = SinglyLinkedList()
list.node_append(10)
list.node_append(20)

list.print_list()