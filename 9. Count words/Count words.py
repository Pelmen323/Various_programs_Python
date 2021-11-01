from tkinter import filedialog, Tk
import string
from collections import Counter
from timeit import default_timer as timer


def count_words():
    window = Tk()
    try:
        with open(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]), 'r', encoding='utf-8') as file:
            text_file = file.read()
    except Exception:
        print('Unable to open file')
        return

    window.destroy()
    start = timer()
    for i in text_file:
        if i in string.punctuation:
            text_file = text_file.replace(i, '')

    text_file = text_file.replace('\n', '').lower()
    text_split = [i for i in text_file.split(' ') if i != '']
    words_dict = (
        sorted(dict(Counter(text_split)).items(), key=lambda x: -x[1]))

    print("Total words: " + str(len(text_split)))
    print("Unique words: " + str(len(words_dict)))
    print("Count\tword")
    for i in words_dict:
        print(f"{i[1]}:\t{i[0]}")
    stop = timer()
    print(f"The run is finished in {stop-start:.4f} seconds")


if __name__ == '__main__':
    count_words()
    input("Press any key to exit ")
