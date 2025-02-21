# 이진 트리 구현

# 초기화
memory = []
root = None

class TreeNode(): 
    def __init__(self):
        self.head = None
        self.nodes = []

    class Node():
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
    def insert(self):
        new_node = self.Node()
        new_node.data = self.nodes
        for name in self.nodes:
            self.data = name
            print(self.data)

    def find(self, find_data):
        findNode = None
        self.nodes[0]

t = TreeNode()
t.insert()


    # if __name__ == '__main__':
    #     node = TreeNode()
    #     node.data = nameAry[0]
    #     root = node
    #     memory.append(node)

    #     for name in nameAry[1:]:
    #         node = TreeNode()
    #         node.data = name

    #         current = root
    #         while True:
    #             if name < current.data: # 현재 name이 노드의 데이터보다 작으면
    #                 if current.left == None:
    #                     current.left = node
    #                     break # 연결했으니 반복문 탈출
    #                 else:
    #                     current = current.left # 왼쪽으로 더 내려감
    #             else: # 오른쪽으로 보냄
    #                 if current.right == None:
    #                     current.right = node
    #                     break
    #                 else:
    #                     current = current.right

    #         memory.append(node)
            
    #     print('이진탐색 트리 구성 완료!')