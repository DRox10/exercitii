import tkinter as tk
from tkinter import *
import time
#-------------windows & square1------------------
window = tk.Tk()

WIDTH = 500
HEIGHT = 500


canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

x = 5
y = 5

x1=255
y1=200
square1 = canvas.create_rectangle(x1, y1, x1+70, y1+70, fill="red", outline='red') # center position 


x2=185
y2=195
square2 = canvas.create_rectangle(x2, y2, x2+70, y2+70, fill="blue", outline='blue') 

x3=255
y3=270
square3 = canvas.create_rectangle(x3, y3, x3+70, y3+70, fill="green", outline='green')

x4=180
y4=276
square4 = canvas.create_rectangle(x4, y4, x4+70, y4+70, fill="yellow", outline='yellow')

#-------------move&loop ----------

def move():
        canvas.move(square1, 5, -57/10) #RED            
        canvas.move(square2, -5, -54/10 ) #BLUE
        canvas.move(square3, 5, 5) #GREEN      
        canvas.move(square4, -5, 4) #YELLOW 
        canvas.after(20, move)
move()
window.mainloop()
        