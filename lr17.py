from tkinter import *

year = 2003


def on_click():
    global year
    year -= 2
    # buttonText.set(f'Chupyna, {year}')
    btn.config(text=f'Chupyna, {year}')


root = Tk()
root.title("Group 202")
root.geometry('400x350')

# buttonText = StringVar()
# buttonText.set(f'Chupyna, {year}')

btn = Button(
    # textvariable=buttonText,
    text=f'Chupyna, {year}',
    command=on_click,
    padx=25,
    pady=10,
    foreground='#FF00FA',
    background='#406080',
    font=16
)
btn.pack()

root.mainloop()
