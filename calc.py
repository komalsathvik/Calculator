from tkinter import *
from PIL import Image,ImageTk
from math import *
root=Tk()
root.geometry("400x500")
def get_result(event, value):
    current_text = entry.get()
    if value == "=":
        try:
            result = eval(current_text, {"__builtins__": None}, {"sin": lambda x: sin(radians(x)), "cos": lambda x: cos(radians(x)), "log": log})
            entry.delete(0, END)
            entry.insert(0, str(result))
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "Error")
    elif value == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, value)
icon = PhotoImage(file="img.png")
root.iconphoto(False, icon)
entry_font = ("Helvetica", 20)
entry = Entry(root, width=15, font=entry_font)
entry.grid(row=1, column=0, columnspan=4)
buttons = [
    ('9', 2, 0), ('8', 2, 1), ('7', 2, 2),
    ('6', 3, 0), ('5', 3, 1), ('4', 3, 2),
    ('3', 4, 0), ('2', 4, 1), ('1', 4, 2),
    ('0', 5, 0), ('+', 5, 1), ('-', 5, 2), ('*', 4, 3), ('log', 5, 3),('sin',6,0),('cos',6,1),('C',6,2),('=',6,3),
    ('(',2,3),(')',3,3),('/',4,3)
]
for (text, row, column) in buttons:
    button = Button(root, text=text, width=10, height=5)
    button.grid(row=row, column=column)
    button.bind('<Button-1>', lambda event, text=text: get_result(event,text))
root.mainloop()