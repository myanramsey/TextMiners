
#utilize class for sets to make has table like data structre
class structSimulator:
    def __init__(self, key, instances):
        self.key = key
        self.instances = instances

    #utlized to sort objects in the class
    def __gt__(self, less):
        return self.instances < less.instances

class HashTable:
    def __init__(self):
        self.hashTable = set()
        self.bucketValue = 0

    #For every duplicate found, increment by one
    def insert(self, key):
        keyFound = False
        for iter in self.hashTable:
            if key == iter.key:
                iter.instances +=1
                keyFound=True

    #For every new word for an object will be made for it
        if not keyFound:
            y =structSimulator(key, 1)
            self.hashTable.add(y)

    #Will print out the duplicates in order of frequency
    def printInOrder(self):
        t = sorted(self.hashTable)
        for i in t:
            print(f'{i.key}: {i.instances}')

#Charles Code End


