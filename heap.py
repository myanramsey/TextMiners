
#Charles James Jr
#utilize class for sets to make has table like data structre
#Sourced From geeksforgeeks.org https://www.geeksforgeeks.org/heap-sort/

#structre utilized to store both string key and its frequency
class structSimulator:
    def __init__(self, key, instances):
        self.key = key
        self.instances = instances

#class used to constuct heap
class MaxHeap:
    def __init__(self):
        self.size = 0
        self.maxHeap = []

    #function used to heapify array
    def heapify(self, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # less than root
        if r < self.size:
            if self.maxHeap[l].instances < N and self.maxHeap[largest].instances < self.maxHeap[l].instances:
                largest = l

        # See if right child of root exists and is
        # greater than root

        #r needs to be less than size or else there will be an error
        if r < self.size:
            if self.maxHeap[r].instances < N and self.maxHeap[largest].instances < self.maxHeap[r].instances:
                largest = r

        # Change root, if needed
        if largest != i:
            self.maxHeap[i], self.maxHeap[largest] = self.maxHeap[largest], self.maxHeap[i]  # swap

            # Heapify the root.
            self.heapify(N, largest)

    #For every duplicate found, increment by one
    def insert(self, key):
        keyFound = False
        heap = structSimulator(key, 1)
        for index, i in enumerate(self.maxHeap):
            if i.key == heap.key:
                keyFound = True
                self.maxHeap[index].instances +=1
                self.heapify(self.maxHeap[index].instances, 0)

        #if no duplicate is found, add new struct, and put new append at the front of list to heapify it
        if keyFound is False:
            self.size +=1
            self.maxHeap.append(heap)
            i = self.size -1
            while i > 0:
                self.maxHeap[i], self.maxHeap[i -1] = self.maxHeap[i -1], self.maxHeap[i]  # swap
                i-=1
            self.heapify(heap.instances, 0)


    #function utilized to sort heap
    def heapSort(self):
        N = self.size

        # Build a maxheap.
        for i in range(N // 2 - 1, -1, -1):
            self.heapify(N, i)

        # One by one extract elements
        for i in range(N - 1, 0, -1):
            self.maxHeap[i], self.maxHeap[0] = self.maxHeap[0], self.maxHeap[i]  # swap
            self.heapify(i, 0)

    #Will print out the duplicates in order of frequency, top ten and least 10
    def printInOrder(self):
        self.heapSort()
        print("10 Most Common Words:")
        for i in self.maxHeap[len(self.maxHeap)-1:len(self.maxHeap)-11:-1]:
            print(f'{i.key}: {i.instances}')

        print()

        print("10 Least Common Words:")
        for i in self.maxHeap[0:10]:
            print(f'{i.key}: {i.instances}')


