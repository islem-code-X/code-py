from tkinter import *
import os
def files():
    def backend():
        folder_path = entry.get()
        if len(folder_path) == 0:
            print("huh")
            return

        y = 230
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as f:
                file_content = f.readlines()
            def open_window(content=file_content):
                def open_file_window():
                    window = Tk()
                    window.geometry("500x500")
                    window.configure(background="black", relief="groove", bd=5)
                    b = 0
                    for line in content:
                        Label(window, text=line, font="arial 15 bold", foreground="green").place(x=0, y=b)
                        b += 20
                    window.mainloop()

                return open_file_window

            Button(gui, text=file_name,
                   font="arial 15 bold",
                   bg="black",
                   fg="white",
                   relief=RAISED,
                   bd=5,
                   command=open_window()
                   ).place(x=0, y=y)
            y += 40

    gui = Tk()
    gui.title("File")
    gui.geometry("500x500")
    gui.configure(relief="groove",bd=5)
    Label(gui, text="Files",
          relief=RAISED,
          bd=10,
          background="black",
          font="arial 20 bold",
          foreground="green",
          padx=80,
          pady=10,
          ).pack()
    entry=Entry(gui,
                background="black",
                foreground="green",
                font="arial 20 bold",
                highlightbackground="black",
                )
    entry.place(x=100, y=150)
    Button(gui,
           text="Open",
           font="arial 15 bold",
           relief=RAISED,
           bd=4,
           command=backend
           ).place(x=405,y=147)
    Label(gui,text="enter the path folder :",
          font="arial 15 bold",).place(x=100,y=120)
    Label(gui,relief=RAISED,
          bd=5,
          background="black",
          padx=240,
          pady=3,
          ).place(x=0,y=200)
    gui.mainloop()
files()