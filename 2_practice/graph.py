# 그래프 구현 실습

"""

1. 표현방법
    - 딕셔너리, 리스트를 통한 그래프 표현
        - ex ) 0 : [3, 5] -> 0번 정점은 3번과 5번에 연결되어 있다.
        - 메모리 효율적으로 관리가 가능, 탐색이 빠름.

    - 인접행렬을 통한 그래프 표현
        - ex )  0 1 1   -> A - B 연결 , A - C 연결
                1 0 0
                1 0 0
        - 간선이 존재하는지 확인하는 로직의 실행속도가 굉장히 빠름.
        - 메모리를 많이 사용함.

        
    - 깊이 우선 탐색 (dfs)
        - 정의 노드의 가장 깊은 레벨까지 먼저 들어간 뒤, 남은 곳을 탐색한다.
        - 동작 순서, 스택을 활용, 시작정점을 선택한 뒤, 연결된 정점을 조건에 맞게 스택에 넣는다.

    - 가중치란 무엇이고, 왜 필요할까?
    - 가중치 그래프의 코드로서 표현
        - ex ) { 'A' : [('B',2)] , 'B' : [('A',3),('C',4)]}
        - 최단 경로 탐색 등에 필요하다

"""

class graph_hr:
    def __init__(self,size,isList=False):
        self.size = size
        self.isList = isList
        if isList:
            self.graph = {}
        else:
            self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def __str__(self):
        for i in self.graph:
            print(i)
        return ''
    
    def set(self,values = dict):
        # 리스트 버전
        if self.isList:
            self.graph = values
        # 행렬 버전
        else:
            key = list(values.keys())[0]
            value = list(values.values())[0]
            for i in range(self.size):
                self.graph[key][i] = value[i]
                   
# 틈새 특강
graph = graph_hr(4) 

# 리스트 버젼
# graph.set({'A' : ['B','C'], 
#            'B' : ['A','C'], 
#            'C' : ['A','B','D'], 
#            'D' : ['C'] })

# 행렬버젼
graph.set({0 : [0,1,1,0]})
graph.set({1 : [1,0,1,0]})
graph.set({2 : [1,1,0,1]})
graph.set({3 : [0,0,1,0]})


## 딕셔너리 버전 구현




## 인접 행렬 버전 구현
class Graph:
    def __init__(self, size, setting=False):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        if setting:
            self.setting_All_connecting()

    def setting_All_connecting(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    self.graph[i][j] = 1

    def __str__(self):
        return "\n".join(str(row) for row in self.graph)

    def set(self, edge_dict):
        row = list(edge_dict.keys())[0]
        values = list(edge_dict.values())[0]

        if not (0 <= row < self.size):
            raise ValueError(f"유효하지 않은 row 번호입니다: {row}")
        if len(values) != self.size:
            raise ValueError(f"values 길이는 {self.size}이어야 합니다.")

        self.graph[row] = values

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                # 현재 노드(node)의 인접 노드 탐색
                for neighbor in range(self.size - 1, -1, -1):
                    if self.graph[node][neighbor] == 1 and neighbor not in visited:
                        stack.append(neighbor)
        return visited