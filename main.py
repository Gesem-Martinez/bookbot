def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_letters(text):
    count_dict = {}

    for letter in text:
        if letter.isalpha():
            low_letter = letter.lower()
            if low_letter in count_dict:
                count_dict[low_letter] += 1
            else:
                count_dict[low_letter] = 1
    return count_dict



def main():
    with open('./assets/frankenstein.txt', 'r') as file:
        contents = file.read()

        print(count_letters(contents))


main()
