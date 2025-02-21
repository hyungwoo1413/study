"""


class graph_hr:

    def __init__(self, isList = False):
        self.isList = isList
        if isList: 
            print('A', end=' ')
        else:           
            print('B', end=' ')

    def set(self):
        if self.isList: 
            print('가', end='\n')
        else: 
            print('나', end='\n')


graph1 = graph_hr(True) 
graph1.set()

graph2 = graph_hr(False) 
graph2.set()

graph3 = graph_hr()
graph3.set()


"""








list = [[0, 1, 2, 3],[0, 1, 2, 3],[0, 1, 2, 3],[0, 1, 2, 3]]


print(list[2][0])    # list의 인덱스[2][0]의 값

print([2][0])        # [2]의 인덱스[0]의 값

print([10,20,30][2]) # [10,20,30]의 인덱스[2]의 값

