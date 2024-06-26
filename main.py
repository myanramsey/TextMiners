import nltk
from nltk.corpus import stopwords
from collections import Counter
import re
import time

from hashmap import hashMap
from heap import MaxHeap
def get_important_names(text):
    # Get important Names
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(tagged_tokens)

    names = []
    for entity in named_entities:
        if hasattr(entity, 'label') and entity.label() == "PERSON":
            names.append(" ".join(child[0] for child in entity))

    for name in names:
        if name in stopwords.words('english') or (len(name) <= 1):
            names.remove(name)

    return names
def get_most_common_places(text):

    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    places = nltk.ne_chunk(tagged_tokens)

    most_common_places = []

    for place in places:
        if hasattr(place, 'label') and place.label() == "LOCATION":
            most_common_places.append(" ".join(child[0] for child in place))

    return most_common_places
def get_most_common_date(text):

    months = {'January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October', 'November', 'December'}
    date_patterns = [
        r'\b\w+\s\d+,\s\d{4}\b',  # e.g., "January 1, 2023"
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # e.g., "1/1/2023"
        r'\b\d{4}-\d{2}-\d{2}\b'  # e.g., "2023-01-01"
        r'\b\w+\s\d{4}\b'
    ]

    dates = []
    pls_work = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        for i in matches:
            for key in months:
                if key in i:
                    dates.append(i)
    return dates
def printTest(array):
    word_freq = Counter(array)

    # Sort the word frequency in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_word_freq = sorted_word_freq[0:10]

    # Print the word frequency
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq}")

def main():
    print("Welcome to TextMiners! The program where we help analyze your text and give you the most important information about it for studying :) \n"
          "Please choose down below on what textbook you would like to analyze and what information you would like to know.\n")

    book_choice = True
    while(book_choice):
        read_choice = True
        choice = int(input("What file would you like to read?\n"
                           "0. Exit \n"
                            "1.Knowledge for Human's Textbook\n"
                            "2.Romeo and Juliet\n"
                            "3.The American Yawp\n"
                           "Input: "))

        if choice == 1:
            with open('text/Knowledge-For-Humans.txt', 'r',encoding='utf-8') as file:
                text = file.read()
        elif choice == 2:
            with open('text/Romeo-and-Juliet.txt','r',encoding='utf-8') as file:
                text = file.read()
        elif choice == 3:
            with open('text/yawp_v1.txt','r',encoding='utf-8') as file:
                text = file.read()
        elif choice == 0:
            book_choice = False
            read_choice = False

        while(read_choice):
            data_choice = True
            info_choice = int(input("What would you like to analyze?\n"
                                    "0. Exit\n"
                                    "1. Names\n"
                                    "2. Places\n"
                                    "3. Dates\n"
                                    "Input: "))

            print("analyzing book choice...")

            if info_choice == 1:
                arr = get_important_names(text)
            elif info_choice == 2:
                arr = get_most_common_places(text)
            elif info_choice == 3:
                arr = get_most_common_date(text)
            elif info_choice == 0:
                read_choice = False
                data_choice = False

            while(data_choice):

                user_choice = int(input("What data structure would you like to choose?\n"
                                        "1. Hashmap\n"
                                        "2. Min/Max Heap\n"
                                        "3. Exit\n"
                                        "Input: "))
                #Source for time code: https://docs.python.org/3/library/time.html#time.perf_counter_ns
                if(user_choice == 1):
                 # use hashmap to display data
                    start = time.perf_counter_ns()
                    answer = hashMap(arr.__len__())
                    answer.create_buckets()
                    for word in arr:
                        answer.add_Value(word)
                    end = time.perf_counter_ns()
                    print("Results:")
                    answer.print_most_common()
                    print(f'Time Results: {end - start} Nano Seconds')

                elif(user_choice == 2):
                    print("Choice 2")
                # use heap to display data
                    start = time.perf_counter_ns()
                    heap = MaxHeap()
                    for i in arr:
                        heap.insert(i)
                    heap.heap_sort()
                    end = time.perf_counter_ns()
                    heap.print_in_order()
                    print(f'Time Results: {end - start} Nano Seconds')
                elif(user_choice == 3):
                    data_choice = False;
                    read_choice= False;

                # printTest(arr)
                print("------------------------------------")


    print("Thanks for using TextMiners! Hope this information allowed you to see what is important")

if __name__ == '__main__':
    main()




