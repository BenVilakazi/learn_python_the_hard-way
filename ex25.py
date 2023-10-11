def break_words(stuff):
    """This function will break up words for us."""
    print(">>> breakwords")
    words = stuff.split(' ')
    return words 
print("<<< exit")

def sort_words(words):
    """ Sort the words."""
    print(">>> sort words")
    return sorted(words)
print("<<< exit")

def print_first_word(words):
    """Print the first word after poppong it off."""
    print(">>> print first word")
    word = words.pop(0)
    print(word)
    print("<<< exit")
    
def print_last_word(words):
    """Prints the last word after poppong it off"""
    print(">>> print last word")
    word = words.pop(-1)
    print(word)
    print("<<< exit")
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    print(">>> print sorted words")
    words = break_words(sentence)
    return sort_words(words)
print("<<< exit")
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    print(">>> print first and last word")
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    print("<<< exit")
    
def print_first_and_last_sorted(sentence):
    
    """Sorts the words then prints the first and last one"""
    print(">>> print sorted sentence")
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    print("<<< exit")