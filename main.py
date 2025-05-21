from stats import count_words, count_letters, sort_count
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    letters = count_letters(text)
    sorted_letters = sort_count(letters)
    for entry in sorted_letters:
        for letter, count in entry.items():
            print(f"{letter}: {count}")

if __name__ == "__main__":
    main()