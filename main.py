import nltk


def main():
    print("Hello World!")
    with open('text/Knowledge-For-Humans.txt', 'r',encoding='utf-8') as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)

    print(sentences)
    print(words)


main()
