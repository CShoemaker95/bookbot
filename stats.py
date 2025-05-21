import string

def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_letters(text):
    text = text.lower()
    count = {letter: 0 for letter in string.ascii_lowercase}
    for char in text:
        if char in count:
            count[char] += 1
    return count

def sort_count(count):
    items = list(count.items())
    items.sort(key=lambda item: item[1], reverse=True)
    sorted_list = [{letter: count} for letter, count in items]
    return sorted_list
