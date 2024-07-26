from tkinter import *
import calendar

root = Tk()
root.geometry("400x300")
root.title("Calendar")

def text():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int,month_int)
    textfeild.delete(0.0, END)
    textfeild.insert(INSERT, cal)

label_1 = Label(root, text = "Month:")
label_1.grid(row = 0, column = 0)
label_2 = Label(root, text = "Year:")
label_2.grid(row = 0, column = 1)

month = Spinbox(root, from_= 1, to = 12, width = 8)
month.grid(row = 1, column = 0, padx = 5)
year = Spinbox(root, from_= 2000, to = 2100, width = 10)
year.grid(row = 1, column = 1, padx = 10)

button = Button(root, text="Go", command = text)
button.grid(row = 1, column = 2, padx = 10)

textfeild = Text(root, width = 25, height = 10, fg = "red")
textfeild.grid(row = 2, columnspan = 2)


root.mainloop()