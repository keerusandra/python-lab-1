import re
from collections import Counter


def count_specific_word(text, search_word):
   
    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())


def identify_most_common_word(text):

    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return ""

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):

    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0.0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):

    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    if len(paragraphs) == 0:
        return 0
    else:
        return len(paragraphs)


def count_sentences(text):

    sentences = re.findall(r"[.!?]+", text)
    return len(sentences)


def main():
    text = input("Enter a news article:\n")

    search_word = input("Enter a word to search: ")

    print("Specific word count:", count_specific_word(text, search_word))
    print("Most common word:", identify_most_common_word(text))
    print("Average word length:", calculate_average_word_length(text))
    print("Paragraph count:", count_paragraphs(text))
    print("Sentence count:", count_sentences(text))


    answer = "yes"

    while answer.lower() == "yes":
        answer = input("Analyze another article? (yes/no): ")

        if answer.lower() == "yes":
            text = input("Enter a news article:\n")
            search_word = input("Enter a word to search: ")

            print("Specific word count:", count_specific_word(text, search_word))
            print("Most common word:", identify_most_common_word(text))
            print("Average word length:", calculate_average_word_length(text))
            print("Paragraph count:", count_paragraphs(text))
            print("Sentence count:", count_sentences(text))
        else:
            print("Goodbye!")


if __name__ == "__main__":
    main()