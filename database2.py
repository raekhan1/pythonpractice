from tkinter import *

def submit():

def clear():

root = Tk()
root.geometry("270x240")
root.title("Student details")
root.resizable(False, False)
root.configure(background = "Light blue")

frame_heading = Frame(root)
frame_heading.grid(row=0, column=0, columnspan=2, padx=30, pady=5)

frame_entry = Frame(root)
frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

Label(frame_heading, text="Student details form", font=('Arial',16))\.grid(row=0, column=0, padx=0, pady=0)
Label(frame_entry, text="Username: ")\.grid(row=0, column=0, padx=10, pady=5)
Label(frame_entry, text="First name: ")\.grid(row=1, column=0, padx=10, pady=10)
Label(frame_entry, text="Surname: ")\.grid(row=1, column=0, padx=10, pady=10)

username=Entry(frame_entry, width=15, bg="white")
username.grid(row=0, column=1, padx=5, pady=5)

firstname=Entry(frame_entry, width=15, bg="white")
firstname.grid(row=1, column=1, padx=5, pady=5)

surename=Entry(frame_entry, width=15, bg="white")
surname.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
