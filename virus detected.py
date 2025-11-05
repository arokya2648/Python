from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning('Alert', 'Stop! virus found.')
    messagebox.showinfo('Alert', 'Stop! virus found.')
    messagebox.showerror('Alert', 'Stop! virus found.')
    messagebox.askquestion('Alert', 'Stop! virus found.')
    messagebox.askokcancel('Alert', 'Stop! virus found.')
    messagebox.askyesno('Alert', 'Stop! virus found.')
    messagebox.askretrycancel('Alert', 'Stop! virus found.')
button=Button(root, text='Scan for virus', command=msg)
button.place(x=40, y=80)
root.mainloop()