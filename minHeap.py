# MHNode class representing a node in the minimum heap.
class MHNode:
    def __init__(self, ride, rbt, minHeapIndex):
        self.ride = ride #ride object
        self.rbTree = rbt # rbt tree node 
        self.minHeapIndex = minHeapIndex #index of the node in minHeap

#MinHeap class
class MinHeap:
    def __init__(self):
        self.hList = [0]
        self.currentSize = 0

    #insert element in the minHeap
    def insert(self, ele):
        self.hList.append(ele)
        self.currentSize += 1
        self.heapifyUp(self.currentSize)

    #Update element with new key
    def updateElement(self, x, new_key):
        node = self.hList[x]
        node.ride.tripDuration = new_key
        if x == 1:
            self.heapifyDown(x)
        elif self.hList[x // 2].ride.comparator(self.hList[x].ride):
            self.heapifyDown(x)
        else:
            self.heapifyUp(x)

    #delete element at index x from minHeap
    def deleteElement(self, x):

        self.swapNodes(x, self.currentSize)
        self.currentSize -= 1
        *self.hList, _ = self.hList
        self.heapifyDown(x)

    #Remove and return root from minHeap
    def pop(self):
        if len(self.hList) == 1:
            return 'No Rides Available'
        root = self.hList[1]
        self.swapNodes(1, self.currentSize)
        self.currentSize -= 1
        *self.hList, _ = self.hList
        self.heapifyDown(1)
        return root    
    
    #swap nodes at the parameter indices
    def swapNodes(self, index_1, index_2):
        temp = self.hList[index_1]
        self.hList[index_1] = self.hList[index_2]
        self.hList[index_2] = temp
        self.hList[index_1].minHeapIndex = index_1
        self.hList[index_2].minHeapIndex = index_2
    
    # Get the index of the child node with the minimum key.
    def getMinChildIndex(self, x):
        if (x * 2) + 1 > self.currentSize:
            return x * 2
        else:
            if self.hList[x * 2].ride.comparator(self.hList[(x * 2) + 1].ride):
                return x * 2
            else:
                return (x * 2) + 1

    #Move a node up the heap
    def heapifyUp(self, x):
        while (x // 2) > 0:
            if self.hList[x].ride.comparator(self.hList[x // 2].ride):
                self.swapNodes(x, (x // 2))
            else:
                break
            x = x // 2

    #Move a node down the heap
    def heapifyDown(self, x):
        while (x * 2) <= self.currentSize:
            ind = self.getMinChildIndex(x)
            if not self.hList[x].ride.comparator(self.hList[ind].ride):
                self.swapNodes(x, ind)
            x = ind


    
