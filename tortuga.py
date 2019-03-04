import turtle
import time
# from turtle import *
# title ("Primer ventana de tortuga")

window = turtle.Screen().title("Tortuga")
tortuga = turtle.Turtle()
tortuga.pensize(5)
tortuga.pencolor('#000')
tortuga.forward(100)
tortuga.right(180)
tortuga.forward(100)
tortuga.left(180)
tortuga.forward(100)
tortuga.right(180)
tortuga.forward(100)
tortuga.left(90)

time.sleep(10)#Espera de 10 segundo 
window.mainloop()
