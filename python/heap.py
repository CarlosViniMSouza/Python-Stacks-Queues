from heapq import heappop, heappush


class Heap:
    def __init__(self):
        self.fruits = []

    def addElement(self, newData):
        heappush(self.fruits, newData)

    def popElement(self):
        heappop(self.fruits)

    def showHeap(self):
        print(self.fruits)


heap = Heap()

heap.addElement("Carlos")
heap.addElement("Vinicius")
heap.addElement("Monteiro")
heap.addElement("de Souza")

heap.showHeap()

# removing the first element (fruits[0] == "Carlos")
heap.popElement()

heap.showHeap()
