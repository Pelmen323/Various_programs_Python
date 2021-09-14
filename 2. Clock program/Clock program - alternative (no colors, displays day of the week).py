from tkinter import *
import time

window = Tk()

label_time = Label(window, font = ('Helvetica', 40))
label_day = Label(window, font = ('Helvetica', 30))
label_date = Label(window, font = ('Helvetica', 30))

label_time.pack()
label_day.pack()
label_date.pack()

while True:
    label_time.config(text=time.strftime("%H:%M:%S", time.localtime()))
    label_day.config(text=time.strftime("%A",time.localtime()))
    label_date.config(text=time.strftime("%d %B %Y", time.localtime()))
    window.update()
    time.sleep(0.1)

window.mainloop()