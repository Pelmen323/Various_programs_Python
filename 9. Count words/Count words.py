from tkinter import Tk, filedialog
import string

def count_words():
    window = Tk()
    try:                                                                                                            # Open file
        with open(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]), 'r', encoding='utf-8') as file:
            text_file = file.read()
    except: 
        print('Unable to open file')
        return
    window.destroy()                                                                                                # To hide the window that is triggered automatically
    for i in text_file:                                                                                             # Remove all punctuation from string
        if i in string.punctuation:
            text_file = text_file.replace(i, '')

    text_file = text_file.replace('\n', '').lower()                                                                 # Remove newline char and make all words lower
    text_split = [i for i in text_file.split(' ') if i != '']                                                       # Create a clear list with words

    words_dict = dict()
    for word in text_split:
        words_dict.update({word:text_split.count(word)})                                                            # Count the words in file

    sorted_dict = sorted(words_dict.items(), key=lambda x:-x[1])                                                    # Sort the results
    print("Total words: " + str(len(text_split)))
    print("Unique words: " + str(len(words_dict)))
    for i in sorted_dict:
        print(i[0]+":\t\t"+str(i[1]))

if __name__=='__main__':
    count_words()
    input("Press any key to exit ")
    