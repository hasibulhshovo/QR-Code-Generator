import pyqrcode
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import messagebox

root = Tk()  # creating tkinter window
root.title('QR Code Generator')  # setting window title
root.iconphoto(False, PhotoImage(file='icon.png'))  # setting window icon
root.geometry("300x50")  # setting window size


# function to generate and display QR code
def generateQR():
    # getting the text
    text = entry.get()
    # if text field is empty show a warning otherwise show the QR Code
    if not text:
        messagebox.showinfo(title='Warning', message='Enter Something!')
    else:
        var = pyqrcode.create(text)  # creating qr code
        img = "qr-code.png"  # setting image name
        var.png(img, scale=3)  # saving image
        show_qr = PIL.ImageTk.PhotoImage(PIL.Image.open(img))  # opening the QR Code
        # label
        label = Label(root, image=show_qr)
        label.image = show_qr
        root.geometry("300x200")
        label.grid(row=1, column=0, columnspan=2, padx=15, pady=10)


# text field
entry = Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)
# button
button = Button(root, text="Generate", command=generateQR)
button.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
