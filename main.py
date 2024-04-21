import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

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

    # Print the word frequency
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq}")

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
            text = file.read()

    info_choice = int(input("What would you like to analyze?\n"
                            "1. Names\n"
                            "2. Places\n"
                            "3. Dates\n"
                            "Input: "))

    print("loading...")
    if info_choice == 1:
        arr = get_important_names(text)
    elif info_choice == 2:
        arr = get_most_common_places(text)
    elif info_choice == 3:
        arr = get_most_common_date(text)

    printTest(arr)

if __name__ == '__main__':
    main()



