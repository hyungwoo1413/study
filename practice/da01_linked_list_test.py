### 연결 리스트

# 배열 : 메모리가 연속적이며, 추가 및 수정에 오버헤드(컴퓨터가 힘들어해요)가 발생한다.
# 연결 리스트 : 메모리 주소는 상관 없이, 서로가 서로를 가르켜 연결하는 방식, 수정 및 추가, 삭제 등이 매우 간단하고 편리하다.



# 챌린지 1.

# 아래는 제가 구현한 연결리스트 클래스 입니다.
# 한줄 한줄 주석을 달아서 이게 뭔지, 어떤 동작인지 설명해보세요.

class LinkedList:                           # ex: 이 클래스의 이름은 LinkedList 이다.
    def __init__(self):                     # init 메서드 , 클래스가 생성될 때, 실행되는 메서드이다.
        self.head = None                    # 
        self.nodes = []                     # 

    class Node:                             # 새로운 개념 : 이너클래스 (클래스 안의 클래스, 클래스와 개념은 같다.)
        def __init__(self, data):           # init 메서드 , 클래스가 생성될 때, 실행되는 메서드이다.
            self.data = data                # 
            self.prev = None                # 
            self.next = None                # 

        def __str__(self):                  # str 메서드, 이 클래스의 인스턴스를 프린트 하면 메모리주소가 뜨기 때문에, 사람이 볼 수 있는 걸 반환해주는 동작.
            return f"{self.data}"

    def push_back(self, data):              # append 메서드 , 매개변수로 data를 입력 받는다. (리스트의 마지막에 요소를 추가하는 동작)  
        new_node = self.Node(data)          ## 받아온 data를 new_node에 저장
        if not self.head:                   ## 노드가 처음 들어왔으면(헤드가 없으면)
            self.head = new_node            ## head에 첫 노드를 입력
            prevNode = None                 ## 첫 node라서 preNode가 없음
        else:                               ## 처음 들어온 node가 아니면(헤드가 있으면)
            self.nodes[-1].next = new_node  ## 마지막 노드 뒤에 새로운 노드 연결(마지막노드.next -> new_node)
            prevNode = self.nodes[-1]       ## prevNode
        self.nodes.append(new_node)         ## 새로들어온 node를 리스트에 저장
        self.nodes[-1].prev = prevNode      ## nodes 리스트의 가장 마지막 node의 prev에 prevNode 저장
    

    def insert(self,find_data,insert_data): # insert 메서드 , 매개변수로 찾을값, 넣을값을 받고, 리스트의 찾을값이 있는 위치에 넣을값을 넣습니다.
        new_node = self.Node(insert_data)   
        isFind = False                      
        for node in self.nodes:             
            if node.data == find_data:      
                curNode = node              
                isFind = True               
                break
        if isFind == False: return

        if curNode.prev != None:
            new_node.prev = curNode.prev
            curNode.prev.next = new_node
            curNode.prev = new_node
            new_node.next = curNode
        else : 
            self.head = new_node
            new_node.prev = None
            new_node.next = curNode
            curNode.prev = new_node

    def delete(self,del_data):              # delete 메서드, 매개변수로 지울 값을 입력받은 후 검색하여 노드를 삭제합니다.
        for node in self.nodes:
            if node.data == del_data:
                delData = node
                break
            
        if self.head == delData:
            self.head = delData.next
        elif delData.next == None:
            delData.prev.next = None
        else:
            delData.prev.next = delData.next
            delData.next.prev = delData.prev
        del(delData)

    def find(self,find_data):               # find 메서드 , 매개변수로 찾을 값을 입력받은 후 검색하여 노드를 반환합니다.
        findNode = None
        for node in self.nodes:
            if node.data == find_data:
                findNode = node
                break
        return findNode 
        
    def print_list(self):                   # print_list 메서드, 현재 리스트에 존재하는 요소들을 출력합니다.
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next
        print("None")

list1 = LinkedList()
list1.push_back('김씨')
list1.push_back('왕씨')
list1.push_back('철씨')
list1.print_list()
list1.insert('왕씨','옹씨')
list1.print_list()

list2 = LinkedList()
list2.push_back('굼씨')
list2.push_back('진씨')
list2.print_list()
list2.insert('굼씨','주씨')
list2.print_list()