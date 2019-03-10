#Author     : Ishwar Jindal
#Created On : 10-Mar-2019 10:25 AM IST
#Purpose    : this file contain program to draw pie


import turtle
import math

#draw a specified number of pies for said length
def draw_pie(t, sides, length):
    
    angle = 360/sides #peak angle 

    side_angle = (180 - angle) / 2 #each part will be isosceles angle. so side angles will be equal

    side_length = 2 * length * math.cos(math.radians(side_angle)) #This is the formula to get the side length

    t.lt(angle/2)
    for i in range(sides):
        t.fd(length)
        t.lt(180 - side_angle)
        t.fd(side_length)
        t.lt(180 - side_angle)
        t.fd(length)
        t.lt(180)
        
t = turtle.Turtle()
sides = input("Enter sides : ")
length = input("Enter side length : ")

draw_pie(t, int(sides), int(length))
