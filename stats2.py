import string

def count_words(text): # get the word count for the supplied text
    words = text.split() # splits the text by whitespace so each word in the string returns individually
    num_words = len(words) # gives an integer for the length of the words list
    return num_words

def count_letters(text):# gets the letter count for the supplied text
    text = text.lower()#converts all letters to lowercase
    count = {letter: 0 for letter in string.ascii_lowercase} #establishes a dictionary called count with letter:num (string.ascii_lowercase)
    for char in text: #start iterating through the text
        if char in count: #if the iterated letter is in the dict
            count[char] += 1 #increment that part of the dict +=1
    return count #return dict

def sort_count(count): #create function to sort the count based on provided count
    items = list(count.items()) #split count into tuples using list and .items()
    items.sort(key=lambda item: item[1], reverse=True) #.sort with key lambda, item to item[1] and reverse to true
    sorted_list = [{letter:count} for letter, count in items] #create a sorted list of dicts with letter:count for letter, count in items
    return sorted_list # return the sorted list