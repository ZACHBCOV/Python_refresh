#python for begginers Timothy needham
# imports and variables
import math

a = 2
b = 2
c=math.sqrt(a**2+b**2)
print(c)

# loops
for name in "john","sam","jill":
    print("hello" +" "+ name)

for i in range(10):
 print(i)


total = 0
for i in 5, 7, 11, 13:
    print(i+total)
    total=total+i
print(total)
# total added in print i line 3. Without = prints each number as it occurs then totals all. With total
# ... it gives a running total upto the final value i.e. 36. i.e. 5 --> 5+7 ---> 5+7+11---> 5+7+11+13 END

# to indent (i.e. add for spaces = TAB key
    #ENTER CODE HERE
# i in loops stands for 'index' - the index can be replced by any relevant name even _ where we do not
#.. care about the value of 'i'

for _ in range(10):
    print(_ + 1)
    # output = 1-10

list_of_beverages = ["Beer", "wine", "water"]

for drink in list_of_beverages:
    print("would you like a "+drink+"?")


# mooms show

1+1
12*3

print("Hello moons")

x = "hello moons"

print(x)

del x

numbers = [1, 2, 3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

name = "moomin"

for letter in name:
    print(letter)

total=0
for i in 5,6,7,8:
    print(i+total)
    total=total+i
print(total)

import turtle
turtle.forward(50)
turtle.right(50)
turtle.forward(50)
turtle.left(50)
turtle.forward(50)
turtle.left(50)
turtle.forward(50)


# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
    for i in range(200):

        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)

# Defining method to draw a full heart
def heart():

    # Set the fill color to red
    pen.fillcolor('red')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()

# Defining method to write text
def txt():

    # Move turtle to air
    pen.up()

    # Move turtle to a given position
    pen.setpos(-68, 95)

    # Move the turtle to the ground
    pen.down()

    # Set the text color to lightgreen
    pen.color('lightgreen')

    # Write the specified text in
    # specified font style and size
    pen.write("I love you Snoons", font=(
      "Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()

import turtle
for i in range(10):
    turtle.forward(10+5)
    turtle.penup()
    turtle.forward(5+5)
    turtle.pendown()
    i=i+10

#nested loop
import turtle
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
        for i in range(4):
            turtle.forward(50)
            turtle.left(45)
                for i in range(4):
                    turtle.forward(100)
                    turtle.left(90)
                        for i in range(4):
                            turtle.forward(200)
                            turtle.left(180)


#strings
#INDEXING
str = "heya"

print(str[0]) # returns 'h' from the defined string [0] = first position character

print(str[-1]) # returns the last character

print(str[-2]) # returns second from last character

#SLICING

print(str[0:2]) # slicing returns a range within the string. 0 being the firt character. up-to but not
#...including position 2 i.e. he .. if position 2 was inclusive it would return hey.


