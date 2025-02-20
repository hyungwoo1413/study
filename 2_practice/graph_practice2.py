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
graph = graph_hr(4, True) 

# 리스트 버젼
graph.set({'A' : ['B','C'], 
           'B' : ['A','C'], 
           'C' : ['A','B','D'], 
           'D' : ['C'] })

# 행렬버젼
graph.set({0 : [0,1,1,0]})
graph.set({1 : [1,0,1,0]})
graph.set({2 : [1,1,0,1]})
graph.set({3 : [0,0,1,0]})

print(graph)