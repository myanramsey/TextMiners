
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
        self.max_heap = []

    #function used to heapify array
    def heapify(self, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # less than root
        if r < self.size:
            if self.max_heap[l].instances < N and self.max_heap[largest].instances < self.max_heap[l].instances:
                largest = l

        # See if right child of root exists and is
        # greater than root

        #r needs to be less than size or else there will be an error
        if r < self.size:
            if self.max_heap[r].instances < N and self.max_heap[largest].instances < self.max_heap[r].instances:
                largest = r

        # Change root, if needed
        if largest != i:
            self.max_heap[i], self.max_heap[largest] = self.max_heap[largest], self.max_heap[i]  # swap

            # Heapify the root.
            self.heapify(N, largest)

    #For every duplicate found, increment by one
    def insert(self, key):
        keyFound = False
        heap = structSimulator(key, 1)
        for index, i in enumerate(self.max_heap):
            if i.key == heap.key:
                keyFound = True
                self.max_heap[index].instances +=1
                self.heapify(self.max_heap[index].instances, 0)

        #if no duplicate is found, add new struct, and put new append at the front of list to heapify it
        if keyFound is False:
            self.size +=1
            self.max_heap.append(heap)
            i = self.size -1
            while i > 0:
                self.max_heap[i], self.max_heap[i - 1] = self.max_heap[i - 1], self.max_heap[i]  # swap
                i-=1
            self.heapify(heap.instances, 0)


    #function utilized to sort heap
    def heap_sort(self):
        N = self.size

        # Build a maxheap.
        for i in range(N // 2 - 1, -1, -1):
            self.heapify(N, i)

        # One by one extract elements
        for i in range(N - 1, 0, -1):
            self.max_heap[i], self.max_heap[0] = self.max_heap[0], self.max_heap[i]  # swap
            self.heapify(i, 0)

    #Will print out the duplicates in order of frequency, top ten and least 10
    def print_in_order(self):
        self.heap_sort()
        print("10 Most Common Words:")
        for i in self.max_heap[len(self.max_heap) - 1:len(self.max_heap) - 11:-1]:
            print(f'{i.key}: {i.instances}')

        print()

        print("10 Least Common Words:")
        for i in self.max_heap[0:10]:
            print(f'{i.key}: {i.instances}')
