from tkinter import *
import time

window = Tk()
window.geometry('500x150')
window.configure(bg='Black')
window.title("Clock")     

label_time = Label(window, font = ('Helvetica', 40), bg='Black',fg='Green' )
label_date = Label(window, font = ('Helvetica', 30), bg='Black', fg='Green')

label_time.pack()
label_date.pack()

# Variant 1 - after calls

def update():
    label_time.config(text=time.strftime("%H:%M:%S", time.localtime()))
    label_date.config(text=time.strftime("%d %B %Y", time.localtime()))
    window.after(1000, update)

update()
window.mainloop()

# Variant 2 - while loop - causes error but works fine

# while True:
#     label_time.config(text=time.strftime("%H:%M:%S", time.localtime()))
#     label_date.config(text=time.strftime("%d %B %Y", time.localtime()))
#     window.update()
#     time.sleep(0.1)
