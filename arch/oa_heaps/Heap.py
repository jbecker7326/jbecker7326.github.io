'''
Created on Mar 13, 2022

@author: Jennifer Becker
'''


class MinHeap():
    # initialize class
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.heapVector = [None] * self.capacity


    # ensure heap has capacity and if not, double capacity
    def ensureCapacity(self):
        if self.size == self.capacity:
            self.heapVector = self.heapVector + [None] * self.capacity
            self.capacity *= 2


    # return element in heap
    def getElement(self, index):
        # raise error if heap is empty
        if self.size == 0:
            raise AttributeError()
        if index >= self.size:
            return None
        else:
            return self.heapVector[index]


    # return size
    def size(self):
        return self.size


    # add value to heap
    def insert(self, value):
        # ensure capacity
        self.ensureCapacity()
        # insert value at bottom of heap and increment size
        self.heapVector[self.size] = value
        self.size += 1
        # heapify up
        self.percolateUp(self.size-1)


    def percolateUp(self, childIndex):
        # get parent index and continue if current index is not the root node
        parentIndex = (childIndex-1) // 2
        if parentIndex >= 0:
            # if value at index is less than parent, swap values and continue heapify up
            if self.heapVector[childIndex] < self.heapVector[parentIndex]:
                self.heapVector[childIndex], self.heapVector[parentIndex] = self.heapVector[parentIndex], self.heapVector[childIndex]
                self.percolateUp(parentIndex)


    # delete minimum value from heap
    def deleteMin(self):
        # raise error if heap is empty
        if self.size == 0:
            raise AttributeError()
        # replace first value with last value
        self.heapVector[0] = self.heapVector[self.size-1]
        # decrement size
        self.heapVector[self.size-1] = None
        self.size -= 1
        # heapify down
        self.percolateDown(0)


    def percolateDown(self, parentIndex):
        # get child indexes
        leftChildIndex = (2*parentIndex) + 1
        rightChildIndex = (2*parentIndex) + 2
        # check if left child exists and assume it has smaller stored value
        if leftChildIndex < self.size:
            childIndex = leftChildIndex
            # check if right child exists and if it has smaller stored value
            if rightChildIndex < self.size:
                if self.heapVector[rightChildIndex] <= self.heapVector[leftChildIndex]:
                    childIndex = rightChildIndex
            # if smaller child is less than parent, swap and continue heapify down
            if self.heapVector[childIndex] < self.heapVector[parentIndex]:
                self.heapVector[childIndex], self.heapVector[parentIndex] = self.heapVector[parentIndex], self.heapVector[childIndex]
                self.percolateDown(childIndex)

