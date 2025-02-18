
memory = []
head, pre, current = None, None, None
dataArray = ['지민','010-1111-1111'], ['정국','010-2222-2222'], ['뷔','010-3333-3333'], ['슈가','010-4444-4444'], ['진','010-5555-5555']

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end='')
    while current.link != None:
        current = current.link
        print(current.data, end='')
    print()

def makeSimpleLinkedList(namePhone):
    global memory, head, pre, current

if __name__ == '__main__':
    printNodes(head)

