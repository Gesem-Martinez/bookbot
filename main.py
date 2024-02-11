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


def convert_dict(count_dict):
    count_list = []
    for letter in count_dict:
        count_list.append({"letter": letter, "count": count_dict[letter]})
    return count_list


def sort_key(dict):
    return dict["count"]


def print_report(text, path):
    header = f"--- Begin report for {path} ---"
    footer = "--- End report ---"
    word_count_report = f"{count_words(text)} words found in the document \n\n"

    count_list = convert_dict(count_letters(text))
    count_list.sort(reverse=True, key=sort_key)

    print(header)
    print(word_count_report)

    for item in count_list:
        letter = item["letter"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")

    print(footer)


def main():
    path = './assets/frankenstein.txt'
    with open(path, 'r') as file:
        contents = file.read()

        print_report(contents, path)


main()
