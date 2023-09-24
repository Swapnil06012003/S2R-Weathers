from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import cv2
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
import numpy as np
from PIL.ImageFilter import (DETAIL,EMBOSS)


#Home screen defination
window=Tk()
window.config(bg='#29292D')
window.title("Image Processor")



#Screen withdraw
window.withdraw()

def pltsh():
    img = cv2.imread("img1.png", 0)
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(), 256, [0, 255])
    plt.title('histogram')
    plt.show()

def save():
    path= "out.png"
    img=Image.open(path,mode="r")
    file= asksaveasfilename(initialdir="/", title="Select file", filetypes=(
    ('JPEG', ('.jpg', '.jpeg', '.jpe', '.jfif')), ('PNG', '.png'), ('BMP', ('.bmp', '.jdib')), ('GIF', '.gif')),
                            defaultextension=".png")
    path2=file
    img.save(path2)

def showout():
    img = Image.open("out.png")
    displayimg=img
    resized_image = displayimg.resize((300, 205))
    new_image = ImageTk.PhotoImage(resized_image)
    l5.config(image=new_image)
    l5.image = new_image

    b122.config(text="save",command=save)

    l5.place(x=875, y=345)
    b122.place(x=700,y=240)


def removefillist():
    b4.place(x=500, y=-650)
    b5.place(x=500, y=-680)
    b6.place(x=-500, y=-710)
    b61.place(x=-500, y=-710)

    b3.config(command=showfil)

def removemor():
    b8.place(x=840, y=-650)
    b9.place(x=840, y=-680)
    b10.place(x=840, y=-710)
    b11.place(x=840, y=-740)
    b12.place(x=960, y=-650)
    b13.place(x=960, y=-680)
    b14.place(x=960, y=-710)

    b7.config(command=showmor)

def blur():

    img = cv2.imread('rgb.png', 1)
    image_blurred = cv2.blur(src=img, ksize=(20, 20))
    cv2.imwrite("out.png", image_blurred)

    showout()

def sharpen():
    sharp_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])
    img = cv2.imread('rgb.png', 1)
    sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=sharp_kernel)
    cv2.imwrite("out.png", sharp_img)

    showout()

def emboss():
    img = Image.open('rgb.png')
    img1 = img.filter(EMBOSS)
    img1.save('out.png')

    showout()

def smoothen():
    img = Image.open('rgb.png')
    img1 = img.filter(DETAIL)
    img1.save('out.png')

    showout()


def erosion():
    img = cv2.imread('rgb.png',0)
    binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((5, 5), np.uint8)
    invert = cv2.bitwise_not(binr)
    erosion = cv2.erode(invert, kernel,iterations=1)
    cv2.imwrite("out.png", erosion)

    showout()

def dialate():
    img = cv2.imread('rgb.png', 0)
    kernel = np.ones((5, 5), np.uint8)
    img_dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite("out.png", img_dilation)

    showout()

def open():
    img = cv2.imread('rgb.png')
    kernel = np.ones((5, 5), np.uint8)
    image = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite("out.png", image)

    showout()

def close():
    img = cv2.imread('rgb.png')
    kernel = np.ones((5, 5), np.uint8)
    image = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite("out.png", image)

    showout()

def grad():
    img = cv2.imread('rgb.png')
    kernel = np.ones((2, 2), np.uint8)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite("out.png", gradient)

    showout()

def tophat():
    img = cv2.imread('rgb.png')
    filter_size = (5, 5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filter_size)
    image = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    cv2.imwrite("out.png", image)

    showout()

def blackhat():
    img = cv2.imread('rgb.png')
    filter_size = (5, 5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filter_size)
    image = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite("out.png", image)

    showout()

def segment():
    img = cv2.imread('rgb.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imwrite("ob.png", thresh)
    img = Image.open("ob.png")
    img = img.convert("RGB")
    d = img.getdata()
    new_image = []
    for item in d:
        if item[0] in list(range(200, 256)):
            new_image.append((255, 0, 0))
        else:
            new_image.append(item)

    img.putdata(new_image)
    img.save("out.png")

    showout()


def transform():
    img = cv2.imread('rgb.png')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 200, apertureSize=3)
    minLineLength = 10
    maxLineGap = 5
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength, maxLineGap)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite('out.png', img)

    showout()



#Home Screen

def showfil():

    b4.config(text="Blur",command=blur)
    b5.config(text="Sharpen",command=sharpen)
    b6.config(text="Emboss",command=emboss)
    b61.config(text="Detail", command=smoothen)

    b4.place(x=400,y=650)
    b5.place(x=400,y=680)
    b6.place(x=400,y=710)
    b61.place(x=400,y=740)

    b3.config(command=removefillist)

def showmor():
    b8.config(text="Erosion",command=erosion)
    b9.config(text="Dialation",command=dialate)
    b10.config(text="Opening",command=open)
    b11.config(text="Closing",command=close)
    b12.config(text="Gradient",command=grad)
    b13.config(text="Top Hat",command=tophat)
    b14.config(text="Black Hat",command=blackhat)

    b8.place(x=550,y=650)
    b9.place(x=550, y=680)
    b10.place(x=550, y=710)
    b11.place(x=550, y=740)
    b12.place(x=650,y=650)
    b13.place(x=650, y=680)
    b14.place(x=650, y=710)

    b7.config(command=removemor)

def fileselection():

    filepath=filedialog.askopenfilename()
    img = cv2.imread(filepath)
    cv2.imwrite("rgb.png", img)
    img = (Image.open("rgb.png"))
    resized_image = img.resize((300, 205))
    new_image = ImageTk.PhotoImage(resized_image)

    l2.config(image=new_image)
    l2.image = new_image
    l3.config(text="Original preview")
    l4.config(text="Output preview")
    b2.config(text="Histogram", command=pltsh)
    b3.config(text="Filters",command=showfil)
    b7.config(text="Operations",command=showmor)
    b15.config(text="Segment",command=segment)
    b16.config(text="transform",command=transform)

    l2.place(x=300, y=350)
    l3.place(x=345, y=300)
    l4.place(x=920, y=300)
    b2.place(x=700, y=400)
    b3.place(x=400, y=600)
    b7.place(x=600, y=600)
    b15.place(x=800,y=600)
    b16.place(x=1000 , y=600)

def home():

    window.deiconify()
    window.state('zoomed')

    l1.config(text="Select your file",font=('Times New Roman',40),foreground='white')
    l1.place(x=580,y=100)

    b1.config(text="Select",command=fileselection,height=1,width=10,borderwidth = 4)
    b1.place(x=700,y=200)

#Home Screen Labels
l1=Label(window,bg='#29292D')

#Fileselection Labels
l2=Label(window)
l3=Label(window,font=('Times New Roman', 25), foreground='white', bg='#29292D')
l4=Label(window,font=('Times New Roman', 25), foreground='white', bg='#29292D')

#Filter Labels
l5=Label(window)


#Home screen buttons
b1=Button(window,bg='white')
b122=Button(window,bg='white',height=1, width=10, borderwidth=4)

#Fileselection Buttons
b2=Button(window,bg='white',height=1, width=10, borderwidth=4)
b3=Button(window,bg='white',height=1, width=10, borderwidth=4)
b7=Button(window,bg='white',height=1, width=10, borderwidth=4)
b15=Button(window,bg='white',height=1, width=10, borderwidth=4)
b16=Button(window,bg='white',height=1, width=10, borderwidth=4)


#Showing filters buttons
b4=Button(window,bg='white',height=1, width=10, borderwidth=4)
b5=Button(window,bg='white',height=1, width=10, borderwidth=4)
b6=Button(window,bg='white',height=1, width=10, borderwidth=4)
b61=Button(window,bg='white',height=1, width=10, borderwidth=4)

#Showing morphological operators
b8=Button(window,bg='white',height=1, width=10, borderwidth=4)
b9=Button(window,bg='white',height=1, width=10, borderwidth=4)
b10=Button(window,bg='white',height=1, width=10, borderwidth=4)
b11=Button(window,bg='white',height=1, width=10, borderwidth=4)
b12=Button(window,bg='white',height=1, width=10, borderwidth=4)
b13=Button(window,bg='white',height=1, width=10, borderwidth=4)
b14=Button(window,bg='white',height=1, width=10, borderwidth=4)



home()


#Windows mainloop
window.mainloop()