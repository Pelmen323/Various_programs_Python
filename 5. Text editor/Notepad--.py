import webbrowser
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font, messagebox

# The path of the current file is automatically saved. I.e. - you create a new file via save as, then continue editing it - the path will be stored and when clicking on 'Save' - the file will be saved

def open_file():
    global current_path
    try:
        text_field.delete(1.0, END) 
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(filepath, 'r') as file:
            text_field.insert(1.0, file.read())
        current_path = filepath
        window.title('Notepad -- : '+current_path)
    except Exception:
        messagebox.showerror(title='Error', message="Couldn't read the file :(")


def save_file():
    global current_path
    try:
        if current_path != None:
            text = str(text_field.get(1.0, END))
            with open(current_path, 'w') as filepath:      
                filepath.write(text)
        else: save_file_as()
    except:
        messagebox.showerror(title='Error', message="Couldn't save the file :(")


def save_file_as():
    global current_path
    try:
        filepath = filedialog.asksaveasfile(title='Save a file', defaultextension='.txt', filetypes=[("Text files", "*.txt")]) 
        if filepath is None:                                        # To avoid error on exiting
            return  
        text = str(text_field.get(1.0, END))
        filepath.write(text)
        filepath.close()
        current_path = filepath.name                                # We need only 'name' part, without encoding or mode
        window.title('Notepad -- : '+current_path)
    except:
        messagebox.showerror(title='Error', message="Couldn't save the file :(")

def cut():
    text_field.event_generate('<<Cut>>')

def copy():
    text_field.event_generate('<<Copy>>')

def paste():
    text_field.event_generate('<<Paste>>')

def change_font_color():
    text_field.configure(fg=colorchooser.askcolor(title='Pick font color')[1])

def change_background_color():
    text_field.configure(bg=colorchooser.askcolor(title='Pick background color')[1])

def change_font(*args):                     # May or may not receive an argument
    text_field.configure(font=(font_name.get(), font_size_chooser.get()))

def get_help():
    # I couldn't resist :)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def about():
    messagebox.showinfo(title='About Notepad--', message='I have no idea what to add here')

def quit_program():
    window.destroy()

window = Tk()
window.title('Notepad --')
window.geometry('500x500')

current_path = None
font_name = StringVar(window)
font_name.set('Times New Roman')
font_size = StringVar(window)
font_size.set('14')

# Top menu section

menubar=Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)                                                  # Create a submenu for menubar, Get rid of - - - - - - line
menubar.add_cascade(label='File', menu=file_menu)                                     # Add Dropdown name for the menu
file_menu.add_command(label='Open', command=open_file, compound=LEFT)                 # Add options for dropdown
file_menu.add_command(label='Save', command=save_file, compound=LEFT)
file_menu.add_command(label='Save as', command=save_file_as, compound=LEFT)
file_menu.add_separator()                                                             # Adds a separator line
file_menu.add_command(label='Exit', command=quit_program, compound=LEFT)                      # A command to quit the window

edit_menu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Edit', menu=edit_menu)                                     # Add Dropdown name for the menu
edit_menu.add_command(label='Cut', command=cut, compound=LEFT)                  # Add options for dropdown
edit_menu.add_command(label='Copy', command=copy, compound=LEFT)
edit_menu.add_command(label='Paste', command=paste, compound=LEFT)

help_menu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Help', command=get_help, compound=LEFT)
help_menu.add_command(label='About the program', command=about, compound=LEFT)


# Text configuration

frame = Frame(window, width=15)
# Dropdown with all possible fonts. Uses font_name variable
font_chooser = OptionMenu(frame, font_name, *font.families(), command=change_font)               # Using all fonts from font.families
font_chooser.pack(side=LEFT)

# Select a font size from the spinbox. Uses font_size vazr
font_size_chooser = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
font_size_chooser.pack(side=LEFT)

# Buttons to pick colors
color_chooser= Button(frame, text='Font color', width=15, command=change_font_color).pack(side=LEFT)
background_color_chooser= Button(frame, text='Background color', width=15, command=change_background_color).pack(side=LEFT)
frame.grid(row=0, column=0)

# Scrollbar and text_field placement
text_field = Text(window, font=(font_name.get(), int(font_size.get())))
scroll_bar_y = Scrollbar(text_field)  
window.grid_rowconfigure(1, weight=1)       # To make it autofill. 1 because we have frame, that should not be expanded
window.grid_columnconfigure(0, weight=1)    # To make it autofill
text_field.grid(sticky=N+E+S+W)             # Text field will stick to this sides when expanding

scroll_bar_y.pack(side=RIGHT, fill=Y)
text_field.configure(yscrollcommand=scroll_bar_y.set)


window.mainloop()