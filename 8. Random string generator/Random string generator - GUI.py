from tkinter import *
import random
import string
from idlelib.tooltip import Hovertip
# random.choice doesn't accept lists, only string
russian_alphabet_upper = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
russian_alphabet_lower = 'йцукенгшщзхъфывапролджэячсмитьбюё'


def copy():
    window.clipboard_clear()
    # -1 to remove newline char
    window.clipboard_append(text_field_output.get(1.0, END)[:-1])
    copy_btn.config(text='Text copied!', state=NORMAL)


window = Tk()
window.title('Random string generator')
# Defining variables for checkboxes
letters_upper = BooleanVar()
letters_upper.set(True)

letters_lower = BooleanVar()
letters_lower.set(True)

letters_rus_upper = BooleanVar()
letters_rus_upper.set(False)

letters_rus_lower = BooleanVar()
letters_rus_lower.set(False)

digits = BooleanVar()
digits.set(True)

punctuation = BooleanVar()
punctuation.set(False)
# Frame - input, settings and button
frame = Frame(window)

info_lbl = Label(frame, text='Hover for info!      ')
Hovertip(info_lbl, "Hi! The program can generate the string of any length with various symbols. Github - https://github.com/Pelmen323/Various_programs_Python \n\n'Copy' button will copy everything in the text field to clipboard, you don't need to select anything\n\nWhen generating >50k symbols, the text will be automatically copied to clipboard\nWhen generating big strings (>1m), it may take some time\nWhen generating strings over 5m symbols, the program will generate 5m symbols and then copy and paste the result until it reaches the desired length.\nTested on 1b string. Prepare your RAM :)", hover_delay=500)
info_lbl.pack(side=LEFT)

lbl_length = Label(frame, text='Set the length of generated string: ')
lbl_length.pack(side=LEFT)

set_length = Entry(frame, width=10)
# Default length is set to 25
set_length.insert(0, '25')
set_length.pack(side=LEFT)

Checkbutton(frame, text="English letters (Uppercase)",
            variable=letters_upper, onvalue=True, offvalue=False).pack(side=LEFT)
Checkbutton(frame, text="English letters (Lowercase)",
            variable=letters_lower, onvalue=True, offvalue=False).pack(side=LEFT)
Checkbutton(frame, text="Russian letters (Uppercase)",
            variable=letters_rus_upper, onvalue=True, offvalue=False).pack(side=LEFT)
Checkbutton(frame, text="Russian letters (Lowercase)",
            variable=letters_rus_lower, onvalue=True, offvalue=False).pack(side=LEFT)
Checkbutton(frame, text="Digits", variable=digits,
            onvalue=True, offvalue=False).pack(side=LEFT)
Checkbutton(frame, text="Special symbols", variable=punctuation,
            onvalue=True, offvalue=False).pack(side=LEFT)


def generate_string():
    # Set the length
    if set_length.get().isdigit():
        length = int(set_length.get())
    else:
        text_field_output.delete(1.0, END)
        text_field_output.insert(1.0, "Invalid string length")
        return

        # Safecheck
    if letters_upper.get() is False and letters_lower.get() is False and digits.get() is False and punctuation.get() is False and letters_rus_upper.get() is False and letters_rus_lower.get() is False:
        text_field_output.delete(1.0, END)
        text_field_output.insert(1.0, "At least 1 checkbox should be selected")
        return
    # High probability of freezes if displaying >50k symbols
    if length < 50000:
        # Conditions for various settings combinations
        text_field_output.delete(1.0, END)
        text_field_output.insert(1.0, ''.join(random.choice((string.ascii_uppercase if letters_upper.get() is True else '') +
                                                            (string.ascii_lowercase if letters_lower.get() is True else '') +
                                                            (string.digits if digits.get() is True else '') +
                                                            (string.punctuation if punctuation.get() is True else '') +
                                                            (russian_alphabet_upper if letters_rus_upper.get() is True else '') +
                                                            (russian_alphabet_lower if letters_rus_lower.get() is True else '')) for i in range(length)))
        copy_btn.config(text='Copy output', state=NORMAL)
    elif length < 5000000:
        text_field_output.delete(1.0, END)
        text_field_output.insert(
            1.0, 'Your text is not printed to avoid freezes. It is automatically copied to clipboard')
        x = ''.join(random.choice((string.ascii_uppercase if letters_upper.get() is True else '') +
                                  (string.ascii_lowercase if letters_lower.get() is True else '') +
                                  (string.digits if digits.get() is True else '') +
                                  (string.punctuation if punctuation.get() is True else '') +
                                  (russian_alphabet_upper if letters_rus_upper.get() is True else '') +
                                  (russian_alphabet_lower if letters_rus_lower.get() is True else '')) for i in range(length))
        window.clipboard_clear()
        window.clipboard_append(x)
        copy_btn.config(text='Text copied!', state=DISABLED)
    else:
        x = ''.join(random.choice((string.ascii_uppercase if letters_upper.get() is True else '') +
                                  (string.ascii_lowercase if letters_lower.get() is True else '') +
                                  (string.digits if digits.get() is True else '') +
                                  (string.punctuation if punctuation.get() is True else '') +
                                  (russian_alphabet_upper if letters_rus_upper.get() is True else '') +
                                  (russian_alphabet_lower if letters_rus_lower.get() is True else '')) for i in range(5000000))
        x = x*round(length/5000000)
        window.clipboard_clear()
        window.clipboard_append(x)
        text_field_output.delete(1.0, END)
        text_field_output.insert(
            1.0, 'Your text is not printed to avoid freezes. It is automatically copied to clipboard.')
        copy_btn.config(text='Text copied!', state=DISABLED)


generate_btn = Button(frame, width=10, text='Generate!',
                      command=generate_string)
generate_btn.pack(side=LEFT)

copy_btn = Button(frame, width=10, text='Copy output', command=copy)
copy_btn.pack(side=LEFT)
frame.pack()

text_field_output = Text(window, borderwidth=5, relief=SUNKEN)
# Note - don't assign the scrollbar to the text field - border letters will be hidden
scroll_bar = Scrollbar(window, orient=VERTICAL,
                       command=text_field_output.yview)
# Assigning the scrollbar
text_field_output.configure(yscrollcommand=scroll_bar.set)

text_field_output.pack(side=LEFT, expand=1, fill='both')
scroll_bar.pack(side=LEFT, fill=Y)

window.mainloop()
