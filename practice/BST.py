# da03_binary_tree.py

# 이진 탐색 트리 (BST) 구현
class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        result = []
        self._inorder(self.root, result)
        return " -> ".join(map(str, result))

    class TreeNode:        
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    # ---------------
    # 트리에 노드 추가
    # ---------------
    def append(self, data):
        node = self.TreeNode(data)

        if self.root is None:
            self.root = node
            print('루트 노드 설정 실행완료')
            return

        parent = self.root
        while True:
            if data < parent.data:  # 왼쪽 서브트리로 이동
                if parent.left is None:
                    parent.left = node
                    print(f'왼쪽 자식 추가: {data}')
                    break
                else:
                    parent = parent.left
            else:  # 오른쪽 서브트리로 이동
                if parent.right is None:
                    parent.right = node
                    print(f'오른쪽 자식 추가: {data}')
                    break
                else:
                    parent = parent.right

    # ---------------
    # 전위 순회 (Preorder Traversal)
    # ---------------
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        print(" -> ".join(map(str, result)))

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    # ---------------
    # 중위 순회 (Inorder Traversal)
    # ---------------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        print(" -> ".join(map(str, result)))

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

    # ---------------
    # 후위 순회 (Postorder Traversal)
    # ---------------
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        print(" -> ".join(map(str, result)))

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.data)
    
    # ---------------
    # 탐색
    # ---------------
    def find(self, findName):
        current = self.root
        while current:
            if findName == current.data:
                print(f'{findName} 찾음')
                return current
            elif findName < current.data:
                current = current.left
            else:
                current = current.right
        
        print(f'{findName}(이/가) 트리에 없음')
        return None

    # ---------------
    # 삭제
    # ---------------
    def delete(self, delName):
        self.root = self._delete_recursive(self.root, delName)

    def _delete_recursive(self, node, delName):
        if node is None:
            print(f'{delName}(이/가) 트리에 없음')
            return node

        if delName < node.data:
            node.left = self._delete_recursive(node.left, delName)
        elif delName > node.data:
            node.right = self._delete_recursive(node.right, delName)
        else:
            print(f'{delName} 삭제 진행')

            # 애 없음
            if node.left is None and node.right is None:
                return None
            
            # 자식 한놈
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # 자식 두놈
            successor = self._find_min(node.right) ## 왜냐 
            node.data = successor.data  
            node.right = self._delete_recursive(node.right, successor.data)  # 후계자 노드 삭제

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node


if __name__ == '__main__':    
    nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']            
    mytree = Tree()
    for name in nameAry:
        mytree.append(name)

    print("\n트리 출력 (중위 순회):")
    mytree.inorder()

    print("\n전위 순회:")
    mytree.preorder()

    print("\n후위 순회:")
    mytree.postorder()

    print("\n탐색 테스트:")
    mytree.find('마마무')
    mytree.find('방탄소년단')

    print("\n삭제 테스트:")
    mytree.delete('마마무')
    mytree.inorder()
