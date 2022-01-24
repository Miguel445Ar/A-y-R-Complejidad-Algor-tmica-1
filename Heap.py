class Heap:
    def __init__(self,comp):
        self.hp = []
        self.size = 0
        self.comp = comp
    def push(self,value):
        self.hp.append(value)
        self.size += 1
        self._heapifyForInsertion()
    def pop(self):
        if self.size == 0:
            return None
        value = self.hp[0]
        self.hp[0] = self.hp[self.size - 1]
        self.hp.pop()
        self.size -= 1
        self._heapifyForDeletion()
        return value
    def _heapifyForInsertion(self):
        if self.size <= 1:
            return
        index = self.size - 1
        parent = (index - 1) // 2
        while self.comp(self.hp[index],self.hp[parent]):
            self.hp[index], self.hp[parent] = self.hp[parent], self.hp[index]
            if parent == 0:
                break
            index = parent
            parent = (index - 1) // 2
    def _heapifyForDeletion(self):
        if self.size <= 1:
            return
        index = 0
        lChild = 2 * index + 1
        rChild = 2 * index + 2
        minPos = 0

        if lChild > (self.size - 1):
            minPos = rChild
        elif rChild > (self.size - 1):
            minPos = lChild
        else:
            minPos = lChild if self.comp(self.hp[lChild],self.hp[rChild]) else rChild

        while self.comp(self.hp[minPos],self.hp[index]):
            self.hp[index], self.hp[minPos] = self.hp[minPos], self.hp[index]
            index = minPos
            lChild = 2 * index + 1
            rChild = 2 * index + 2
            if lChild > (self.size - 1) and rChild > (self.size - 1):
                break
            elif lChild > (self.size - 1):
                minPos = rChild
            elif rChild > (self.size - 1):
                minPos = lChild
            else:
                minPos = lChild if self.comp(self.hp[lChild],self.hp[rChild]) else rChild

    def getHeap(self):
        return self.hp
    def Size(self):
        return self.size
