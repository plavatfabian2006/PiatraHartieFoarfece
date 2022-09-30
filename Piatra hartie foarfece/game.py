from email.mime import image
from fileinput import filename
import tkinter
from tkinter import ttk
from tracemalloc import stop
from turtle import back, bgcolor, right
from typing import Container
import tk
import imghdr
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import numpy as np 
import pygame
from PIL import Image,ImageTk
import os
import time
import pyautogui
from PIL import Image, ImageTk


lst=["assets\Foarfece stanga.png","assets\piatra stanga.png","assets\hartie stanga.png"]
m=0
n=0
hscore=0
pygame.font.init()
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED=200
score1=0
score2=0
ok=0


def foarfece():
    z=random.randint(0,2)
    global score1
    global score2
    img1=PhotoImage(file=lst[z])
    my_image=canvas.create_image(400,250,anchor=NW,image=img1)
    ok=1
    img=PhotoImage(file="assets\Foarfece dreapta.png")
    my_image=canvas.create_image(50,250,anchor=NW,image=img)
    if score1==3:
        won()
    if score2==3:
        game_over()
    if z==2:
        score1+=1
        label.config(text="Player Score:{}".format(score1))
    if z==1:
        score2+=1
        label2.config(text="Comp Score:{}".format(score2))
    time()


def piatra():
    z=random.randint(0,2)
    global score1
    global score2
    img1=PhotoImage(file=lst[z])
    my_image=canvas.create_image(400,250,anchor=NW,image=img1)
    ok=2
    img=PhotoImage(file="assets\piatra dreapta.png")
    my_image=canvas.create_image(50,250,anchor=NW,image=img)
    if score1==3:
        won()
    if score2==3:
        game_over()
    if z==0:
        score1+=1
        label.config(text="Player Score:{}".format(score1))
    if z==2:
        score2+=1
        label2.config(text="Comp Score:{}".format(score2))
    time()


def hartie():
    z=random.randint(0,2)
    global score1
    global score2
    img1=PhotoImage(file=lst[z])
    my_image=canvas.create_image(400,250,anchor=NW,image=img1)
    ok=3
    img=PhotoImage(file="assets\hartie dreapta.png")
    my_image=canvas.create_image(50,250,anchor=NW,image=img)
    if score1==3:
        won()
    if score2==3:
        game_over()
    if z==1:
        score1+=1
        label.config(text="Player Score:{}".format(score1))
    if z==0:
        score2+=1
        label2.config(text="Comp Score:{}".format(score2))
    time()
   

def game_over():
    canvas.delete(ALL)
    P["state"] = DISABLED 
    H["state"] = DISABLED
    F["state"] = DISABLED
    canvas.config(background='black')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="You LOST",fill="red",tag="You LOST")
    canvas.pack()


def won():
    canvas.delete(ALL)
    P["state"] = DISABLED 
    H["state"] = DISABLED 
    F["state"] = DISABLED 
    canvas.config(background='black')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="You WON",fill="white",tag="You WON")
    canvas.pack()


window=Tk()
window.title("BlackJack")
window.resizable(False,False)


label_frame = tk.Frame()
label_frame.pack(side = 'top', fill = 'x')


label= tkinter.Label(label_frame, text="Player Score:" ,font=('consolas',15))
label.config(text="Player Score:{}".format(score1))
label.pack(side = 'left', ipadx = 2, ipady = 1,padx=80)
label2= tkinter.Label(label_frame, text="Comp Score:" ,font=('consolas',15))
label2.config(text="Comp Score:{}".format(score2))
label2.pack(side = 'left', ipadx = 2, ipady = 1,padx=70)


label.pack()
label2.pack()


canvas=Canvas(window, bg='green',height=GAME_HEIGHT,width=GAME_WIDTH)
imgi=PhotoImage(file="assets\Bara.png")
my_image=canvas.create_image(350,0,anchor=NW,image=imgi)


button_frame = tk.Frame()
button_frame.pack(side = 'bottom', fill = 'x')


P = tkinter.Button(button_frame, text ="Piatra",background='red', command = piatra)
P.pack(side = 'left', ipadx = 3, ipady = 1,padx=90)
H = tkinter.Button(button_frame, text ="Hartie",background='blue', command = hartie)
H.pack(side = 'left', ipadx = 3, ipady = 1,padx=80)
F = tkinter.Button(button_frame, text ="Foarfece",background='green', command = foarfece)
F.pack(side = 'left', ipadx = 3, ipady = 1,padx=80)


P.pack()
H.pack()
F.pack()


canvas.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.mainloop()
