import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import numpy as np
import pytesseract
from PIL import Image
from gtts import gTTS
import os

root = tk.Tk()
root.configure(background="Orchid3")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.state('zoomed')
root.title("Image Processing")

image2 = Image.open('bg.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

lbl = tk.Label(root, text="", font=('times', 35, ' bold '), height=1, width=30, bg="grey", fg="white")
lbl.place(x=500, y=2)

IMAGE_SIZE = 150

frame_display = tk.LabelFrame(root, text=" --Display-- ", width=1400, height=470, bd=5, font=('times', 10, ' bold '),
                              bg="white")
frame_display.grid(row=0, column=0, sticky='nw')
frame_display.place(x=180, y=60)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=180, height=950, bd=5, font=('times', 10, ' bold '),
                           bg="grey")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=5, y=0)



def clear_img():
    img11 = tk.Label(frame_display, background='white', width=160, height=120)
    img11.place(x=0, y=0)


def update_label(str_T):
    clear_img()
    result_label = tk.Label(frame_display, text=str_T, width=50, font=("bold", 20), bg='white', fg='blue')
    result_label.place(x=0, y=0)

def openimage():
    global fn
    clear_img()
    fileName = askopenfilename(initialdir='/data', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE = 400
    imgpath = fileName
    fn = fileName

    img = Image.open(imgpath)
    img = img.resize((IMAGE_SIZE, 120))

    img = np.array(img)
    x1 = int(450)
    y1 = int(70)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    img = tk.Label(frame_display, text='Orignal', compound=tk.BOTTOM, image=imgtk, font=('times', 15, ' bold '),
                   height=200, width=450)
    img.image = imgtk
    img.place(x=10, y=2)

def imgtospecch():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(fn)
    with open('abc.txt', mode='w') as file:
        file.write(result)
        print(result)
        T= Text(frame_display,height=100,width=200)
        t1 = tk.Label(frame_display, text="Image to speech")
        t1.config(font=('times', 14))
        t=tk.Label(frame_display,text=result)
        t.config(font=('times',27))
        t1.pack()
        t.pack()
        T.pack()

        myobj = gTTS(text=result,
                     lang="en",
                     slow=False)

        myobj.save("convert.wav")
        os.system("convert.wav")
        #engine = pyttsx3.init()
        #engine.say(result)
        #engine.runAndWait()


def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text=" Select Image ", command=openimage, width=13, height=2,
                        font=('times', 15, ' bold '), bg="burlywood2", fg="black")
button1.place(x=5, y=50)

button2 = tk.Button(frame_alpr, text="Image to \n Speech", command=imgtospecch, width=13, height=2,
                    font=('times', 15, ' bold '), bg="burlywood2", fg="black")
button2.place(x=5, y=150)

exit = tk.Button(frame_alpr, text="Exit", command=window, width=13, height=1, font=('times', 15, ' bold '), bg="black",
                 fg="burlywood2")
exit.place(x=5, y=500)

root.mainloop()
