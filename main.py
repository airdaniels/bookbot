def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = text_count(text)
    num_chars = char_count(text)
    sorted_chars = chars_to_sorted_list(num_chars)
        
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document!" + "\n")
    for c in sorted_chars:
        if not c["char"].isalpha():
            continue
        print(f"The {c["char"]} character was found {c["num"]} times!")
    print("--- End Report ---")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def text_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    letters = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in letters:
            letters[char_lower] +=1
        else:
            letters[char_lower] = 1
    return(letters) 

def sort_on(d):
    return d["num"]

def chars_to_sorted_list(num_chars_dict):
    sorted_list= []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()