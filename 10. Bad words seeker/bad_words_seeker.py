##########################
# Word seeker program. Finds all matches and prints where they were found
# By Pelmen, https://github.com/Pelmen323
##########################
import os
import glob
# Dict with wrong_word : right_word. Bad versions are keys in the dict
from bad_words import bad_words
import string


def count_words():
    # Full filepath should be used
    files_path = input("Please enter full filepath to the desired folder: ")
    try:
        os.chdir(files_path)
    except Exception:
        print("Unable to open the folder")

    # Open each .yml file
    for file in glob.glob("*.yml"):
        try:
            # 'utf-8-sig' is mandatory for UTF-8 w/BOM
            with open(file, 'r', encoding='utf-8-sig') as text_file:
                # Extract contents of the file
                text_file = text_file.read()
        except Exception as ex:
            print(f'Skipping the file {file}')
            print(ex)
            continue

        # Remove all punctuation from the text
        for i in text_file:
            if i in string.punctuation:
                text_file = text_file.replace(i, ' ')

        # Split the text by the lines
        text_file = text_file.lower().split("\n")
        # For line index and line text in enumerate(text) - returns line index and line contents
        for i, line in enumerate(text_file):
            # For each word in splitted line (splitting by whitespaces)
            for word in line.split(' '):
                if word in bad_words.keys():
                    print(f'File {file} -- "{word}" in line {i+1} - correct is "{bad_words.get(word)}"')


if __name__ == '__main__':
    count_words()
    while True:
        if input("Press 1 to restart, press any other key to exit: ") == '1':
            count_words()                 # Restart as much as you need
        else:
            break
