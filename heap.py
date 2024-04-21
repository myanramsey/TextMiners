
#utilize class for sets to make has table like data structre
class structSimulator:
    def __init__(self, key, instances):
        self.key = key
        self.instances = instances

    #utlized to sort objects in the class
    def __gt__(self, less):
        return self.instances < less.instances

class MaxHeap:
    def __init__(self):
        self.maxHeap = []

    #For every duplicate found, increment by one
    def insert(self, key, frequency):
        heap = structSimulator(key, frequency * -1)
        self.maxHeap.append(heap)
    #     keyFound = False
    #     for iter in self.hashTable:
    #         if key == iter.key:
    #             iter.instances +=1
    #             keyFound=True
    #
    # #For every new word for an object will be made for it
    #     if not keyFound:
    #         y =structSimulator(key, 1)
    #         self.hashTable.add(y)
    def Heapify(self):
        heapq.heapify(self.maxHeap)

    #Will print out the duplicates in order of frequency
    def printInOrder(self):
        t = self.maxHeap
        while t.__sizeof__() != 0:
            x = heapq.heappop(self.maxHeap)
            print(f'{x.key}: {x.instances}')