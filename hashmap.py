

# used to change the string index into a useable key in the map
# used code from geeksForGeeks: https://www.geeksforgeeks.org/hash-map-in-python/# and data structure from class and/or slides
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
        self.most_common = ""
        self.common_count = 0

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def add_Value(self, key):

        # using the hash function to get the index
        hashed_key = hash_function(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False

        index = -1  # Initialize index outside the loop
        for idx, record in enumerate(bucket):
            record_key, record_val = record
        # check if the bucket has same key as the key to be inserted
            if record_key == key:
                found_key = True
                index = idx  # Set index if the key is found
                break

        # if the key to be inserted is in the bucket then increment the value
        # else add to the value with a count of 1
        if found_key:
            bucket[index] = (key, record_val + 1)
        else:
            bucket.append((key, 1))

        # finding the most frequent word in the hash map
        if bucket[index][1] > self.common_count:
            self.most_common = key
            self.common_count = bucket[index][1]

    def print_most_common(map):
        most_common_words = []
        least_common_words = []

        for bucket in map.hash_table:
            for key, value in bucket:
                if len(most_common_words) < 10:
                    most_common_words.append((key, value))
                    most_common_words.sort(key=lambda x: x[1], reverse=True)

                else:
                    if value > most_common_words[-1][1]:
                        most_common_words.pop()
                        most_common_words.append((key, value))
                        most_common_words.sort(key=lambda x: x[1], reverse=True)

                if len(least_common_words) < 10:
                    least_common_words.append((key, value))
                    least_common_words.sort(key=lambda x: x[1], reverse=True)
                else:
                    if value < least_common_words[-1][1]:
                        least_common_words.pop()
                        least_common_words.append((key, value))
                        least_common_words.sort(key=lambda x: x[1])

        print("10 most common words:")
        for i, count in most_common_words:
            print(f"{i}: {count}")

        print("\n10 least common words:")
        for i, count in least_common_words:
            print(f"{i}: {count}")
