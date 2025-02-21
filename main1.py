from tkinter import *
from PIL import ImageTk, Image
import pygame

from keygen import rand_key

# button event function
def clicked():
    res = rand_key()
    canvas.itemconfig(lbl, text=res)


    # pygame for music
pygame.mixer.init()

pygame.mixer.music.load('02 - anachro - a sad touch.mp3')
pygame.mixer.music.play(-1) # -1 for music loop


                # main window

root = Tk()
root.title("Syberia Key Generator")
#root.geometry('300x300')

        # load image 
img = Image.open('Syberia_back.png')
width = img.size[0]
height = img.size[1]
img = ImageTk.PhotoImage(img)

        # canvas for background image 
canvas = Canvas(root, width=width, height=height)
canvas.pack(side='top', fill='both', expand='no')

canvas.create_image(0, 0, anchor='nw', image=img)


        # text for key
lbl = canvas.create_text(338, 50, text='XXXX-XXXX-XXXX-XXXX', fill='White', font='Impact 17')

        # button widget
btn = Button(root, text='generate', bg ='white', fg='dark blue', command=clicked)
canvas.create_window((308, 70), anchor="nw", window=btn)



root.mainloop()

pygame.mixer.music.stop()