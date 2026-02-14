import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def openFile():
    root = Tk()

    def file():
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        messagebox.showinfo(title="File Opened", message="are you sure?")
        entry.delete(0, END)
        entry.insert(0, file_path)

    root.geometry("300x300")
    root.title("py to exe")
    root.resizable(width=0, height=0)

    Label(root,
          text="py to exe",
          font=("arial", 20, "bold")).pack(side=TOP)

    Frame(root, width=299,
          height=299,
          relief=RAISED,
          bd=3).pack(side=TOP)

    Button(root,
           text="open",
           background="#A1A1A1",
           font="arial 15 bold",
           command=file,
           padx=30).place(y=50, x=90)

    entry = Entry(root, width=30, font="arial 13 bold")
    entry.place(y=100, x=10)

    l = IntVar(value=1)

    def submit():
        file_path = entry.get()
        if not file_path:
            return
        if l.get() == 0:
            cmd = f'pyinstaller --onefile --noconsole "{file_path}"'
        else:
            cmd = f'pyinstaller --onefile "{file_path}"'
        os.system(cmd)

    def mithods():
        Frame(root, width=280, height=70, relief=RAISED, bd=3).place(y=130, x=10)
        y = 150
        x = 40
        Radiobutton(root, text="no console", variable=l, value=0).place(y=y, x=x)
        x = x + 120
        Radiobutton(root, text="with console", variable=l, value=1).place(y=y, x=x)

    mithods()

    Button(root,
           text="Submit",
           background="#4CAF50",
           fg="white",
           font="arial 13 bold",
           command=submit,
           padx=40).place(y=220, x=70)

    root.mainloop()

openFile()
