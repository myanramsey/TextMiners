

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
