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

    word_freq = Counter(sorted_named_entities)

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
            text = file

    print("loading...")
    get_important_names(text)

main()
