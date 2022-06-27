from tkinter import *


def click():
    entry_2.delete(0, 'end')
    entry_2.insert(0, entry_1.get())


root = Tk()
root.title("Chupyna, 202")
root.geometry("500x300")

name_label = Label(text="Entered name")
button = Button(text="Input your name", command=click)
entry_1 = Entry(width=30)
entry_2 = Entry(width=30)

entry_1.pack()
button.pack()

name_label.pack()
entry_2.pack()

root.mainloop()
