##########################
# Word seeker program. Finds all matches and prints where they were found
# By Pelmen, https://github.com/Pelmen323
##########################
import os, glob
from bad_words import bad_words                                                                             # Dict with wrong_word : right_word. Bad versions are keys in the dict
import string

def count_words():
    files_path = input("Please enter full filepath to the desired folder: ")                                # Full filepath should be used
    try:
        os.chdir(files_path)
    except:
        print("Unable to open the folder")
                                                                                                    
    for file in glob.glob("*.yml"):                                                                         # Open each .yml file
        try:
            with open(file, 'r', encoding='utf-8-sig') as text_file:                                        # 'utf-8-sig' is mandatory for UTF-8 w/BOM
                text_file = text_file.read()                                                                # Extract contents of the file
        except Exception as ex:
            print(f'Skipping the file {file}')                                                              
            print(ex)
            continue
                                                                                                                    
        for i in text_file:                                                                                 # Remove all punctuation from the text
            if i in string.punctuation:
                text_file = text_file.replace(i, ' ')

        text_file = text_file.lower().split("\n")                                                           # Split the text by the lines
        for i, line in enumerate(text_file):                                                                # For line index and line text in enumerate(text) - returns line index and line contents
            for word in line.split(' '):                                                                    # For each word in splitted line (splitting by whitespaces)
                if word in bad_words.keys():                                                                
                    print(f'File {file} -- "{word}" in line {i+1} - correct is "{bad_words.get(word)}"') 

if __name__=='__main__':
    count_words()
    while True:
        if input("Press 1 to restart, press any other key to exit: ") == '1': count_words()                 # Restart as much as you need
        else: break