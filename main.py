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

#string operators:

#concatenation
print('hello''world')

S='hello'
r='world'
print(S+r)


# count letters == 'i'

count = 0

for letter in 'thisword':
    if(letter=='i'):
        count=count+1
        #count=count+1 ... can also be written count+=1
print(count, 'letters  i found in the word thisword')


# count letters that are not 'i'

count = 0

for letter in 'thisword':
    if(letter != 'i'):
        count=count+1
        #count=count+1 ... can also be written count+=1
print(count, 'letters which are not i found in the word thisword')


#substring membership test

'a' in 'apple' # >>> True
'a' in 'bluebell' #>>> False


p# Built in fuctions: LEN & Enumerate

list = [ 'one',  'day', 'i' ,'will' 'be', 50 ,'years','old', 'assuming', 'i', 'do', 'not', 'die']

P = 'forget'

#ENUMERATE EXAMPLE
del list
STRING = 'HELPMEFORTHELOVEOFGOD'

list_enumerate = list(enumerate(STRING))
print('LIST_ENUMERATE(STRING)=',list_enumerate)
#OUTPUT = LIST_ENUMERATE(STRING)= [(0, 'H'), (1, 'E'), (2, 'L'), (3, 'P'), (4, 'M'), (5, 'E'), (6, 'F'), (7, 'O'), (8, 'R'), (9, 'T'), (10, 'H'), (11, 'E'), (12, 'L'), (13, 'O'), (14, 'V'), (15, 'E'), (16, 'O'), (17, 'F'), (18, 'G'), (19, 'O'), (20, 'D')]

#THIS ASSIGNS A TUPLE - showing the list position and the letter within this position

print(len(STRING))
#OUTPUT 21

###########Continue 6.10.23 page 47 ... "Python string formatting" ###################################


# 06.10.23
# this displays one type of input as another. This uses a plceholder {} to replace key values
# format methods -

#formatting integers:

print('binary represemtation of {0} is {0:b}'.format(12))

'binary represemtation of {0} is {0:b}'.format(12)
# output = 'binary represemtation of 12 is 1100'


# Formatting floats

'exponent representation: {0:e}'.format(123.234)

#output = 'exponent representation: 1.232340e+02'


#escape sequences in strings:

#1 new line:

print('this is printed in\n two lines')
#Out
# this is printed in
 #two lines

print("i said \"whats theres?!\"") # to use quotes in the output

 # to use back slashes

print("C:\\python32lib\\") # OUT = C:\python32lib\


print("You have {} apple{}.".format(5, 's'))

# this will print:
# You have 5 apples.



#round off
'one third is:{0:.3f}'.format(1/3)
# OUT = 'one third is:0.333'

'{:.5}'.format('xylophone')
# out = 'xylop'
LIST_a = [1,2,3,4,5]
print(LIST_a.pop(1))


# LIST COMPREHENSION = creating new lists uing a for statement.

pow2 = [2** x for x in range (10)]
print (pow2)

# output for pow 2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# THE ABOVE CODE IS EQUIVALENT TO:
pow2_0=[] # Empty list
for x in range(10):
    pow2_0.append(2 ** x)

print(pow2_0)

# if statments - conditions introduce into results


pow3 = [3** x for x in range (10)]
print(pow3)
#out = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]

# for value in position x to the power of 3 i.e. x= 1*3 = 3, x.2 = 3*3 = 9, x.3 = 9*3 = 27  , x.4 = 27*3 etc
# Condition on 7 being greater than 7 as it iterates through the 10 values 0 - 9 for (10)
pow3_0 = [3 ** x for x in range (10) if x > 7]
print (pow3_0)
#out = [6561, 19683]


#odd

odd = [x for x in range(20) if x % 2 == 1]

print(odd)

# OUT  = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# Even
even = [x for x in range(20) if x % 2 == 0]
print(even)

#OUT == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# DICITONARIES

# = unordered collection of items, dictionaries map keys to values - i.e. value key pairs (KEY: VALUE)
#other compund types of data only contain a single value as an element.
# dicitonaries are optimised to return a value when we know the key.
# dictionaries store realted data and are constucted using curly brackets '{}'


# Example
sammy = {'username':'sammy-shark', 'online':True, 'followers':987}

print(sammy)

#OUT = {'username': 'sammy-shark', 'Online': True, 'followers': 987}#
# key value pairs key on the left and value on the right seperated by a colon. When output the order of the dictionary value key pairs may change and this relates to the unordered nature of dictionaries.
# As dictionaries do not maintain order they lack the ability to be indexed. i.e. how you can in tuples or list data types.
#although the dictionaries cannot be indexed, the value key pairs remain intact allowiing the data to be accessed in regard to its relational meaning.


# accessing elements within a dictionary.


print(sammy['followers'])
#OUT = 987

#accessing elements of dictionaries with functions

print(sammy.keys()) # ALLOWS FOR THE ISOLATION OF THE DICTIONARY KEYS
#OUT =dict_keys(['username', 'Online', 'followers'])
print(sammy.values()) # ALLOWS FOR THE ISOLATION OF DICTIONARY VALUES
#OUT =dict_values(['sammy-shark', True, 987])
print(sammy.items()) # ALLOWS FOR THE DISPLAY OF DICTIOANRY TUPLES I.E. VALUE KEY PAIRS.
#OUT =dict_items([('username', 'sammy-shark'), ('Online', True), ('followers', 987)])

# this provides an iterable view across dictionaries, see below.

#new dictionary = Jesse

jesse = {'username':'Jesseeeee', 'online':False, 'followers':101}

print(jesse.keys())

#OUT = dict_keys(['username', 'online', 'followers'])


for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key],jesse[common_key])


#OUT =

''' 987 101 -  #followers
True False     # online 
sammy-shark Jesseeeee''' # username



for common_key in sammy.keys() & jesse.keys():
    print('These are sammy\'s keys:', sammy[common_key],'These are jesse\'s keys:',jesse[common_key])


#OUT:
'''These are sammy's keys: 987 These are jesse's keys: 101
These are sammy's keys: True These are jesse's keys: False
These are sammy's keys: sammy-shark These are jesse's keys: Jesseeee'''


# would be good to see how on each iteration you can prefix with specific wording for a given iteration .
for key, value in sammy.items():
    print(key, ' is the key value ', value)

#OUT:
''' username  is the key value  sammy-shark
online  is the key value  True
followers  is the key value  987'''



for key, value in jesse.items():
    print(key, ' is the key value ', value)
'''username  is the key value  Jesseeeee
online  is the key value  False
followers  is the key value  101'''

# adding to dictionaries
usernames = {'sammy':'sammy-shark', 'dave': 'delicate_dave', 'Jesse':'Jesseeeee'}

usernames['jhon'] = 'Jhinny'

print(usernames)

# OUT = {'sammy': 'sammy-shark', 'dave': 'delicate_dave', 'Jesse': 'Jesseeeee', 'jhon': 'Jhinny'}

jesse = {'username':'Jesseeeee', 'online':False, 'followers':101}

jesse['followers']=255

print(jesse)

# OUT {'username': 'Jesseeeee', 'online': False, 'followers': 255} --> the 101 followers has sucessfully been updated to 255



###################################################################
###################################################################
###################################################################





# programme for username input.



#step 1 define the original dictionary
usernames = {'sammy':'sammy-shark', 'dave': 'delicate_dave', 'Jesse':'Jesseeeee'}


#STEP 2 : SET A WHILE LOOP
while True:
    print('enter name') # STEP 3 request user to enter name
    name=input() # STEP 4 make the variable 'name' = 'users input'
    if name in usernames:
        print(usernames[name]+ + 'is the username of:', name) # STEP 5 check if the username exists within the dictionary and return the username and the name of the individual.
        #break
    else:
        print('i don\'t have'+ name + '\'s usernames, what is it?')

        username = input() # STEP 6 take the user input for the new username

        usernames[name] = username # STEP 7 assign username value to name key within the dictionary

        print('Data Updated') # STEP 8 print to user that the data was updated.

# DOES NOT SAVE UPDATED VALUES
###################################################################
###################################################################
###################################################################


#VERSION 2 - THIS SAVES INTO THE DICTIONARY THE UPDATED VALUE

#step 1 define the original dictionary
usernames = {'sammy':'sammy-shark', 'dave': 'delicate_dave', 'Jesse':'Jesseeeee'}


#STEP 2 : SET A WHILE LOOP
while True:
    print('enter name') # STEP 3 request user to enter name
    name=input() # STEP 4 make the variable 'name' = 'users input'
    if name in usernames:
        print(usernames[name]+ + 'is the username of:', name) # STEP 5 check if the username exists within the dictionary and return the username and the name of the individual.
        #break
    else:
        print('i don\'t have'+ name + '\'s usernames, what is it?')

        username = input() # STEP 6 take the user input for the new username

        usernames[name] = username # STEP 7 assign username value to name key within the dictionary

        print('Data Updated') # STEP 8 print to user that the data was updated.


#STEP 9 ENSURE TO SELECT CTRL + C IN CONSOLE WINDOW

#STEP 10 PRINT THE DICTIONARY ONCE PROGAMME HAS BEEN EXITED - VALIDATE UPDATED VALUE(S) ARE STORED IN YOUR DICTIONARY

#IN THIS CASE OUTPUT = print(usernames) = {'sammy': 'sammy-shark', 'dave': 'delicate_dave', 'Jesse': 'Jesseeeee', 'liam': 'FIREFLY'}

# i.e. the new user input = NAME = 'liam' USERNAME =  'FIREFLY'


# to delete

del usernames["liam"]

print(usernames)

#OUT = {'sammy': 'sammy-shark', 'dave': 'delicate_dave', 'Jesse': 'Jesseeeee'}

# Liam has been deleted...

#02.11.23:

#chapter 10 boolean logic

# = sets a variable to equal an assigned value ... whereas == evaluates whether a variable is equal to another value or variable
# i.e. = is an assignment operator and == is a comparison operator

# logical operators:
        # and: true if both are true
        # or: true if at least one is true
        # not: true only if false


not((0.2>1.4)and((0.8<3.1)or(0.1==0.1))) -- #compound expression for booloean

#Flow control
grade = 70
if grade >= 70:
    print('pass')
else:
    print ('fail')


#exampele 2
balance = -54
if balance < 0:
    print('your account balance is:£', balance, 'you must deposit adequate funds to correct this or be subject to interest and charges')
else:
    print('your balance is:', balance, 'you can withdraw:£', balance*0.5, 'today')


#ELSE IF STATEMENT --> 'elif'

#exampele 3
balance = 0
if balance < 0:
    print('your account balance is:£', balance, 'you must deposit adequate funds to correct this or be subject to interest and charges')

elif balance == 0:
    print ('your account balance is:£', balance, 'consider depositing funds soon to avoid assuming a negative balance')
else:
    print('your balance is:', balance, 'you can withdraw:£', balance*0.5, 'today')


import pandas as pd
import numpy as np

#Create a DataFrame - using pandas - numpy.

# each np.where ((df.score < x), X GRADE, --> cqaptures the values required (parameters for each respective grade.

d = {                                                # Creating a dict for dataframe
    'StudentName':['Harrison','Jake','Jake','Hayley','John', 'belle'],
    'Score':[64,68,61,86,99,12]}

df = pd.DataFrame(d)   # converting dict to dataframe
                       # Keys get converted to column names and values to column values

#get grade by adding a column to the dataframe and apply np.where(), similar to a nested if


df['Grade'] = np.where((df.Score < 60 ),
                  'F', np.where((df.Score >= 60) & (df.Score <= 69),
                  'D', np.where((df.Score >= 70) & (df.Score <= 79),
                  'C', np.where((df.Score >= 80) & (df.Score <= 89),
                  'B', np.where((df.Score >= 90) & (df.Score <= 100),
                  'A', 'No Marks')))))
print(df)

'''
OUTPUT: 
 StudentName  Score Grade
0    Harrison     64     D
1        Jake     68     D
2        Jake     61     D
3      Hayley     86     B
4        John     99     A
5       belle     12     F
'''

#name = str(input('Enter your name'))
marks = int(input('enter your marks'))
while True:             # Loop continuously
    marks = int(input())   # Get the input
    if marks > 90:
        print ('pass grade: A. mark achived over grade threshold:',marks - 90)
    elif marks > 80:
        print ('pass grade: B. mark achived over grade threshold:', marks - 80)
    elif marks > 70:
        print ('pass grade: C. mark achived over grade threshold:', marks - 70)
    elif marks > 60:
        print ('pass grade: D. mark achived over grade threshold:', marks - 60)
    elif marks > 50:
        print ('pass grade: E. mark achived over grade threshold:', marks - 50)
    else:
        print ('Fail grade: F. mark achived under pass grade threshold:', 50 - marks)
    if marks == "":       # If it is a blank line...
            break           # ...break the loop

