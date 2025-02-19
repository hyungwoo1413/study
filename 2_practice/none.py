# 객체지향 구조 연습
# 단순 연결 리스트

class Node:
    def __init__(self, data):
        self.data = data  # 노드가 저장할 데이터
        self.next = None  # 다음 노드를 가리키는 포인터

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 시작을 가리키는 포인터

    def insert(self, data):
        """리스트의 맨 앞에 새로운 노드를 삽입합니다."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """리스트에서 주어진 값을 가진 첫 번째 노드를 삭제합니다."""
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def search(self, key):
        """리스트에서 주어진 값을 가진 노드를 찾습니다."""
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        """리스트의 모든 노드를 순서대로 방문합니다."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 사용 예시
sll = SinglyLinkedList()
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.traverse()  # Output: 3 -> 2 -> 1 -> None
sll.delete(2)
sll.traverse()  # Output: 3 -> 1 -> None
print(sll.search(1))  # Output: True
print(sll.search(4))  # Output: False