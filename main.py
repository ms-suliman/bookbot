from string import ascii_lowercase


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_count(text)} words in document")
    print (" ")
    letters = letter_count(text)

    for letter in letters:
        print (f"The '{letter[0]}' was found {letter[1]} times")



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(to_count):
    words = to_count.split()
    count = len(words)
    return count

def letter_count(to_count):

    # Block only for letters.
    words = to_count.lower()
    letters = {}

    for c in ascii_lowercase:
        letters[c] = words.count(c)

    
    return sorted(letters.items(),key=lambda x:x[1],reverse=True)

    #Block for all characters
    # chars = {}
    # for c in to_count:
    #     lowered = c.lower()
    #     if lowered in chars:
    #         chars[lowered] += 1
    #     else:
    #         chars[lowered] = 1
    # return chars

main()