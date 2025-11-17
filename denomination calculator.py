from tkinter import *
from tkinter import messagebox
from PIL import Image, imageTk
root=Tk()
root.title=('Denomnination Calculator')
root.comfigure(bg  ='light blue')
root.geometry=('650x400')
upload =Image.open('app_img.jpg')
upload = upload.resize((300, 300))
image = imageTk.Photoimage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1 = Label(root, text='Hey user! Welcome to denomination calculator application', bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTRE)
def msg():
    Msgbox = messagebox.showinfo('Alert', 'Do you want to calculate the denominationm count?')
    if Msgbox== 'ok':
        topwin()
button1= Button(root, text='lets get started!', command=msg, bg='browm', fg='white')
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title('Denominations calculator')
    top.comfigure(bg='light grey')
    top.geometry('600x350+50+50')
    label = Label(top, text='Enter total amount', bg='Light grey')
    entry=Entry(top)
    lbl = Label(top, text='Here are number')