def count_words(input_string):
    if input_string.strip() == "":
        return 0
    words = input_string.split()
    return len(words)

def main():
    print("Welcome to the Word Counter program!")
    print("This program counts the number of words in a sentence or paragraph.")

    # Get user input
    sentence = input("Enter a sentence or paragraph: ")
    
    # Count words
    word_count = count_words(sentence)
    
    # Display word count
    if word_count == 0:
        print("Error: Please enter a valid sentence or paragraph.")
    else:
        print(f"Word count: {word_count}")

if _name_ == "_main_":
    main()