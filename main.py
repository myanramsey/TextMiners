import nltk
from nltk.corpus import stopwords
from collections import Counter

def get_important_names(text):
    # Get important Names
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(tagged_tokens)

    names = []
    for entity in named_entities:
        if hasattr(entity, 'label') and entity.label() == "PERSON":
            names.append(" ".join(child[0] for child in entity))

    sorted_named_entities = sorted(names)
    for name in sorted_named_entities:
        if name in stopwords.words('english') or (len(name) <= 1):
            sorted_named_entities.remove(name)

    print(sorted_named_entities)
    #Following code used to test set classes
    # x = HashTable()
    # for i in sorted_named_entities:
    #     x.insert(i)
    # x.printInOrder()


    word_freq = Counter(sorted_named_entities)

    # Sort the word frequency in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Print the word frequency
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq}")


# used to change the string index into a useable key in the map
# used code from geeksForGeeks: https://www.geeksforgeeks.org/hash-map-in-python/#
def hash_function(s):
    # uses separate chaining to deal with collsions
    hash_value = 0
    for char in s:
        hash_value += ord(char)  # adds ASCII value of each character
    return hash_value
class hashMap:

    #creating the map
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        self.most_common = "";
        self.common_count = 0;

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def add_Value(self, key, count):

        # using the hash function to get the index
        hashed_key = hash_function(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

        # check if the bucket has same key as the key to be inserted
            if record_key == key:
                found_key = True
                break

        # if the key to be inserted is in the bucket then increment the value
        # else add to the value with a count of 1
        if found_key:
            count += 1
            bucket[index] = (key, count)
        else:
            bucket.append((key, 1))

        # finding the most frequent word in the hash map
        if count > self.common_count:
            self.most_common = key
            self.common_count = count

    def print_most_common (map):
        print(f"The word '{map.most_common}' shows up the most, with a count of {map.common_count}.")


#Charles Code Start

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



def main():
    print("Hello World!")
    choice = int(input("What file would you like to read? "))
    if choice == 1:
        with open('text/Knowledge-For-Humans.txt', 'r',encoding='utf-8') as file:
            text = file.read()
    elif choice == 2:
        with open('text/Romeo-and-Juliet.txt','r',encoding='utf-8') as file:
            text = file.read()
    elif choice == 3:
        with open('text/yawp_v1.txt','r',encoding='utf-8') as file:
            text = file

    print("loading...")
    get_important_names(text)




if __name__ == '__main__':
    main()



