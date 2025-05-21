import sys
from stats2 import count_words, count_letters, sort_count #type: ignore

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main(): #create func main()
    if len(sys.argv) != 2: #check if length of sysargv not equal to 2 
        print("Usage: python3 redo.py <path_to_book>") #print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #exit via sys code 1
    
    filepath = sys.argv[1] #set filepath to sys.argv entry 1
    text = get_book_text(filepath) #call get book text with input filepath, set to text variable
    word_count = count_words(text) #call imported count_words with input text, variable word_count
    print(f"Found {word_count} total words")
    letters = count_letters(text) #call count_letters input text, variable letters
    sorted_letters = sort_count(letters) # call sort_count with input letters, variable sorted_letters
    for entry in sorted_letters: #iterate for entries in sorted letters
        for letter, count in entry.items(): #for letter, count in itemized entry
            print(f"{letter}: {count}") #print f string of letter:count

if __name__ == "__main__":
    main()
