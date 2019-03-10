#Author     : Ishwar Jindal
#Created On : 09-Mar-2019 07:35 PM IST
#Purpose    : this file contain program to draw flowers


import turtle
import math

#polygon using for loop
def draw_ploygon(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

#draw arc 
def draw_arc(t, r, angle):
    
    circumfrence = 2 * (math.pi) * r * (angle/360)

    #for a circle the number of side of polygon should be a large number
    number_of_sides = 50

    #FORMULA
    #length * number of sides(n) = circumfrence
    
    length_of_each_side = circumfrence/number_of_sides

    draw_ploygon(t, length_of_each_side, number_of_sides, angle)

#draw a petal
def draw_petal(t, radius, angle):
    draw_arc(t, radius, angle)
    t.rt(180+angle)
    draw_arc(t, radius, angle)


#draw a simple flower
def draw_flower(t, radius, angle):
    for i in range(int(360/angle)):
        draw_petal(t, radius, angle)
        t.rt(180)

#draw a crossing flower
def draw_crossing_flower(t, radius, angle):
    for i in range(int(2 * 360/angle)):
        draw_petal(t, radius, angle)
        t.rt(180 + angle/2)
    
t = turtle.Turtle()
radius = input("Enter Radius : ")
angle = input("Enter Angle : ")
should_petal_overlap = input("You want petals overlap? Y/N : ")

#angle = 90
#radius = 100
if (should_petal_overlap == 'Y'):
    draw_crossing_flower(t, int(radius), int(angle))
else:
    draw_flower(t, int(radius), int(angle))    
