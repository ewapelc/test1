#zadanie 5
import tkinter as tk
from PIL import Image, ImageTk

def grey_scale(im):
    img_w, img_h = im.width, im.height
    for x in range(img_w):
        for y in range(img_h):
            r, g, b = im.getpixel( (x,y) )
            grey = int((r+g+b)/3)
            im.putpixel( (x,y), (grey,grey,grey) )

global_var = 0

gui = tk.Tk()
gui.geometry("600x600")
canvas = tk.Canvas(gui, width=500, height=500)

pilimage = Image.open('image.jpg')
greyimage = Image.open('image.jpg')
grey_scale( greyimage )

tkimage = ImageTk.PhotoImage(pilimage)
tkgrey = ImageTk.PhotoImage(greyimage)

w, h = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
c1 = canvas.create_image(w/2,h/2,  image=tkimage)
canvas.pack()

label = tk.Label(gui, text='ghjh', bg='lightblue')
label.pack()

def change_scale():
    global global_var
    global_var += 1
    canvas.itemconfig(c1, image=tkgrey)

def show_details():
    if global_var == 0:
        img = pilimage
    else:
        img = greyimage
    img.show()
    w, h = img.width, img.height
    r, g, b = greyimage.getpixel( (5,10) )
    temp = (r,g,b)
    label.config(text=str(w) + "x" + str(h) + ", kolor piksela (5,10) to " + str(temp) )

button1=tk.Button(gui, text = 'Grey', command=change_scale)
button1.pack()
button2=tk.Button(gui, text = 'Details', command=show_details)
button2.pack()

gui.mainloop()
