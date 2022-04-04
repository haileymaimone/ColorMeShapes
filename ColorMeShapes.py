import tkinter as tk
from tkinter import *

####### GLOBAL VARIABLE DECLARATIONS  NEEDED IN FUNCTIONS #######

# COUNTING GAME VARIABLES
threeTri1 = 'white'
threeTri2 ='white'
threeTri3= 'white'
fourSquare1 ='white'
fourSquare2 ='white'
fourSquare3 ='white'
fourSquare4 ='white'
oneOval = 'white'
fiveRect1 = 'white'
fiveRect2 = 'white'
fiveRect3 = 'white'
fiveRect4 = 'white'
fiveRect5 = 'white'

# COLOR GAME VARIABLES
colorYellowCircle = 'yellow'
colorYellowSquare = 'yellow'
colorRedCircle = 'red'
colorRedOval = 'red'
colorRedRect = 'red'
colorBlueOval = 'blue'
colorBlueRect = 'blue'
colorBlueSquare = 'blue'
colorBlueTriangle = 'blue'
colorOrangeCircle = 'orange'
colorOrangeTri = 'orange'
colorGreenRect = 'green'
colorGreenTriangle = 'green'
colorPurpleOval = 'purple'
colorPurpleRect = 'purple'

# ELEPHANT COLOR VARIABLES
colorLeftEar = 'white'
colorRightEar = 'white'
colorEleHead = 'white'
colorEleLeye = 'white'
colorEleReye = 'white'
colorEleRP = 'white'
colorEleLP = 'white'
colorInLear = 'white'
colorInRear = 'white'
colorBody = 'white'
colorEleLeftLeg = 'white'
colorEleRightLeg = 'white'
colorTrunk = 'white'
colorEleGrass = 'white'

# OWL color variables
colorbeak = 'white'
colorLear = 'white'
colorRear = 'white'
colorRPowl = 'white'
colorLPowl = 'white'
colorReyeOwl = 'white'
colorLeyeowl = 'white'
colorOwlBody = 'white'
colorOwlstomach = 'white'
colorOwlHead = 'white'
colorOwlLleg = 'white'
colorOwlRleg = 'white'
owltext = ''
textOwlFrame = ''

# HOUSE color variables
colorGrass = 'white'
colorHouse = 'white'
colorRoof = 'white'
colorDoor = 'white'
colorHandle = 'white'
colorLeftWin = 'white'
colorRightWin = 'white'
colorSun = 'white'

# TRAIN COLOR VARIABLES
colorWheelBar = 'white'
colorChimneyBase = 'white'
colorChimney = 'white'
colorHorBody = 'white'
colorVertBody = 'white'
colorWindow = 'white'
colorOutWheel = 'white'
colorInnerWheel = 'white'
colorFrontWheel = 'white'
colorMiddleWheel = 'white'
colorTriangle = 'white'


##### FUNCTION DEFINITIONS #####

def show_firstNum():        # function to go back to
    global number_frame     # the first welcome screen
    global first_screen     # from the number frame
    
    first_screen.pack(fill = 'both', expand = 1)
    number_frame.forget()

def show_first_C():         # function to go back to
    global color_frame      # the first welcome screen
    global first_screen     # from color frame

    first_screen.pack(fill = 'both', expand = 1)
    color_frame.forget()
    
def show_main_F():          # function to go back to
    global main_frame       # the first welcome screen
    global first_screen     # from the color shapes main menu
    
    first_screen.pack(fill = 'both', expand = 1)
    main_frame.forget()
    
def show_main_O():          # function to go back to
    global main_frame       # color shapes main menu
    global owl_frame        # from owl frame
    
    main_frame.pack(fill = 'both', expand = 1)
    owl_frame.forget()


def show_main_E():          # function to go back to
    global main_frame       # color shapes main menu
    global elephant_frame   # from the elephant frame
    main_frame.pack(fill = 'both', expand = 1)
    elephant_frame.forget()

def show_main_H():          # function to go back to
    global main_frame       # color shapes main menu
    global house_frame      # from the house frame
    main_frame.pack(fill = 'both', expand = 1)
    house_frame.forget()

def show_main_T():          # function to go back to
    global main_frame       # color shapes main menu
    global train_frame      # from the train frame
    main_frame.pack(fill = 'both', expand = 1)
    train_frame.forget()

def show_mainframe(event):  # function to go to 
    global first_screen     # color shapes main menu
    global main_frame       # from the welcome screen
    
    main_frame.pack(fill = 'both', expand = 1)
    first_screen.forget()

def show_numFrame(event):   # function to go to number game
    global number_frame     # from welcome screen
    global first_screen

    number_frame.pack(fill='both', expand=1)
    first_screen.forget()

def show_colorFrame(event): # function to go to color game
    global color_frame      # from welcome screen
    global first_screen
    
    color_frame.pack(fill = 'both', expand = 1)
    first_screen.forget()

def show_owl(event):        # function to jump to owl picture
    global main_frame
    global owl_frame

    owl_frame.pack(fill = 'both', expand = 1)
    main_frame.forget()
    
def show_elephant(event):   # function to jump to elephant picture
    global main_frame
    global elephant_frame
    elephant_frame.pack(fill = 'both', expand = 1)
    main_frame.forget()
    
def show_house(event):      # function to jump to house picture
    global main_frame
    global house_frame
    house_frame.pack(fill = 'both', expand = 1)
    main_frame.forget()
    
def show_train(event):      # function to jump to train picture
    train_frame.pack(fill = 'both', expand = 1)
    main_frame.forget()

# NUMBER GAME CLICK FUNCTIONS
def numOneClicked(event):   # called when user clicks number 1
    global fiveRect1
    global fiveRect2
    global fiveRect3
    global fiveRect4
    global fiveRect5
    global oneOval
    global numDirText
    global numOOPSText
    
    textonFrame=numberCanvas.itemcget(numDirText, 'text')   # pulls text from top of screen
    
    if textonFrame == 'How many Ovals do you see?':     # if it says 'how many ovals' 
        numberCanvas.itemconfig(numOOPSText, text="Great Job!") # they clicked the correct number
        numberCanvas.delete(oneOval)                    # oval is deleted from screen
        fiveRect1=numberCanvas.create_rectangle(70, 160, 170, 210, fill='purple')   # five rectangles are 
        fiveRect2=numberCanvas.create_rectangle(190, 160, 290, 210, fill='purple')  # placed on screen
        fiveRect3=numberCanvas.create_rectangle(310, 160, 410, 210, fill='purple')  # for next question
        fiveRect4=numberCanvas.create_rectangle(120, 230, 220, 280, fill='purple')  
        fiveRect5=numberCanvas.create_rectangle(250, 230, 350, 280, fill='purple')
        numberCanvas.itemconfig(numDirText, text="How many Rectangles do you see?") # text changes to 'how many rects'
    elif textonFrame != 'How many Ovals do you see?':       # if they click 1 and it is not the correct number
        numberCanvas.itemconfig(numOOPSText, text="OOPS! Try Again!")   # message is displayed 

def numTwoClicked(event):   # called when user clicks number 2
    global numDirText
    global numOOPSText
    global threeTri1
    global threeTri2
    global threeTri3


    textonFrame=numberCanvas.itemcget(numDirText, 'text')   # pulls text from top of screen
    
    if textonFrame == 'How many Circles do you see?':     # if it says 'how many circles' 
        numberCanvas.itemconfig(numOOPSText, text="Great Job!") # they clicked the correct number
        numberCanvas.delete(twoCircles1)        # circles are deleted
        numberCanvas.delete(twoCircles2)        # from screen
        threeTri1=numberCanvas.create_polygon(100, 160, 200, 160, 150, 260, fill='yellow')  # triangles are 
        threeTri2=numberCanvas.create_polygon(300, 160, 400, 160, 350, 260, fill='yellow')  # drawn for next
        threeTri3=numberCanvas.create_polygon(200, 230, 300, 230, 250, 330, fill='yellow')  # question
        numberCanvas.itemconfig(numDirText, text="How many Triangles do you see?")      # text changes for next ?
    elif textonFrame != 'How many Circles do you see?': # if they clicked the wrong number
        numberCanvas.itemconfig(numOOPSText, text="OOPS! Try Again!")

def numThreeClicked(event):   # called when user clicks number 3
    global numDirText
    global numOOPSText
    global threeTri1
    global threeTri2
    global threeTri3
    global fourSquare1
    global fourSquare2
    global fourSquare3
    global fourSquare4


    textonFrame=numberCanvas.itemcget(numDirText, 'text')   # pulls text from top of screen
    
    if textonFrame == 'How many Triangles do you see?':     # if it says 'how many triangles' 
        numberCanvas.itemconfig(numOOPSText, text="Great Job!") # they clicked the correct number
        numberCanvas.delete(threeTri1)        # triangles are deleted
        numberCanvas.delete(threeTri2)
        numberCanvas.delete(threeTri3)
        fourSquare1=numberCanvas.create_rectangle(100, 110, 200, 210, fill='cyan')  # new shapes created
        fourSquare2=numberCanvas.create_rectangle(300, 110, 400, 210, fill='cyan')
        fourSquare3=numberCanvas.create_rectangle(100, 240, 200, 340, fill='cyan')
        fourSquare4=numberCanvas.create_rectangle(300, 240, 400, 340, fill='cyan')
        numberCanvas.itemconfig(numDirText, text="How many Squares do you see?")    # text changes to meet new shapes
    elif textonFrame != 'How many Triangles do you see?':       # if they clicked wrong number
        numberCanvas.itemconfig(numOOPSText, text="OOPS! Try Again!")

def numFourClicked(event):   # called when user clicks number 4
    global numDirText
    global numOOPSText
    global fourSquare1
    global fourSquare2
    global fourSquare3
    global fourSquare4
    global oneOval


    textonFrame=numberCanvas.itemcget(numDirText, 'text')   # pulls text from top of screen
    
    if textonFrame == 'How many Squares do you see?':   # if it says how many 'squares'
        numberCanvas.itemconfig(numOOPSText, text="Great Job!") # user clicked correct number
        numberCanvas.delete(fourSquare1)    # deletes shapes to move
        numberCanvas.delete(fourSquare2)    # to move to next question
        numberCanvas.delete(fourSquare3)
        numberCanvas.delete(fourSquare4)
        oneOval=numberCanvas.create_oval(135, 165, 345, 285, fill='orange') # creates new shapes
        numberCanvas.itemconfig(numDirText, text="How many Ovals do you see?")  # changes text to make new question
    elif textonFrame != 'How many Squares do you see?':     # if they clicked the wrong number
        numberCanvas.itemconfig(numOOPSText, text="OOPS! Try Again!")

def numFiveClicked(event):   # called when user clicks number 4
    global numDirText
    global fiveRect1
    global fiveRect2
    global fiveRect3
    global fiveRect4
    global fiveRect5
    
    textonFrame=numberCanvas.itemcget(numDirText, 'text')   # pulls text from top of screen
    
    if textonFrame == 'How many Rectangles do you see?':   # if it says how many 'rectangles'
        numberCanvas.itemconfig(numOOPSText, text="Great Job!") # user clicked correct number
        numberCanvas.delete(fiveRect1)    # deletes shapes to move
        numberCanvas.delete(fiveRect2)    # to move to next message
        numberCanvas.delete(fiveRect3)
        numberCanvas.delete(fiveRect4)
        numberCanvas.delete(fiveRect5)
        numberCanvas.itemconfig(numDirText, text='Yay!  You have counted 1-5 shapes!', font=('Comic Sans MS', 15, 'bold'))  # user has gone through all 5 numbers
        endText = numberCanvas.create_text(245, 225, text='The End', font=('Impact', 80), justify='center', fill='white')   
    elif textonFrame != 'How many Rectangles do you see?':  # if they clicked the wrong number
        numberCanvas.itemconfig(numOOPSText, text="OOPS! Try Again!")



##### FUNCTIONS FOR COLOR SHAPES GAME #####
# ELEPHANT CLICK FUNCTIONS
def clickEleGrass(event):   # function for when user clicks the grass 
    global my_elephant  # DECLARATIONS FOR ALL GLOBAL VARIABLES NEEDED
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
    
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen
        if textElephantFrame == 'Find the 4 Rectangles!':      # if text asks to find rectangles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a rectangle
            my_elephant.itemconfig(eleGrass, fill="lawn green") # changes the color of rectangle
            colorEleGrass=my_elephant.itemcget(eleGrass, 'fill')    # stores color in variable
        else:   # if the instructions were not to click a rectangle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")   # message appears letting them know
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorEleGrass == 'lawn green' and colorTrunk == 'grey' and colorEleLeftLeg == 'grey' and colorEleRightLeg == 'grey':
            my_elephant.itemconfig(elephanttext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="black")

    
def clickLeftEar(event):    # function for when left ear is clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass

# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen
        if textElephantFrame == 'Find TEN Circles!':      # if text asks to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a circle
            my_elephant.itemconfig(leftear, fill="grey")    # changes the color of circle
            colorLeftEar=my_elephant.itemcget(leftear, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a circle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")
    
def clickRightEar(event):   # function  for when right ear is clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass

# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen and stores it in variable
        if textElephantFrame == 'Find TEN Circles!':      # if text asks to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a circle
            my_elephant.itemconfig(rightear, fill="grey")    # changes the color of circle
            colorRightEar=my_elephant.itemcget(rightear, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a circle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")

def clickEleHead(event):   # function  for when head is clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen and stores it in variable
        if textElephantFrame == 'Find TEN Circles!':      # if text asks to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a circle
            my_elephant.itemconfig(elephant_head, fill="grey")    # changes the color of circle
            colorEleHead=my_elephant.itemcget(elephant_head, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a circle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")


def clickRightLeg(event):   # function acted out if right leg has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen and stores it in variable
        if textElephantFrame == 'Find the 4 Rectangles!':      # if text asks to find rectangles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a rectangle
            my_elephant.itemconfig(rightleg, fill="grey")    # changes the color of rectangle
            colorEleRightLeg=my_elephant.itemcget(rightleg, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a rectangle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorEleGrass == 'lawn green' and colorTrunk == 'grey' and colorEleLeftLeg == 'grey' and colorEleRightLeg == 'grey':
            my_elephant.itemconfig(elephanttext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="black")

def clickLeftLeg(event):   # function acted out if left leg has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen and stores it in variable
        if textElephantFrame == 'Find the 4 Rectangles!':      # if text asks to find rectangles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a rectangle
            my_elephant.itemconfig(leftleg, fill="grey")    # changes the color of rectangle
            colorEleLeftLeg=my_elephant.itemcget(leftleg, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a rectangle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorEleGrass == 'lawn green' and colorTrunk == 'grey' and colorEleLeftLeg == 'grey' and colorEleRightLeg == 'grey':
            my_elephant.itemconfig(elephanttext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="black")

def clickInsideRight(event):   # function acted out if inside of right ear has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen and stores it in variable
        if textElephantFrame == 'Find TEN Circles!':      # if text asks to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")     # they clicked a circle
            my_elephant.itemconfig(inside_rightear, fill="pink")    # changes the color of circle
            colorInRear=my_elephant.itemcget(inside_rightear, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a circle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")


def clickInsideLeft(event):  # function acted out if inside of left ear has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')
        if textElephantFrame == 'Find TEN Circles!':      # if text asks to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!") # they clicked correct shape
            my_elephant.itemconfig(inside_leftear, fill="pink")    # changes the color of circle
            colorInLear=my_elephant.itemcget(inside_leftear, 'fill')      # stores color in variable
        else:   # if the instructions were not to click a circle
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")



def clickEleBody(event):  # function acted out if body has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')    # pulls text from top of screen
        if textElephantFrame == 'Find TEN Circles!':    # if text asked them to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!") # they clicked on a circle
            my_elephant.itemconfig(elephantbody, fill="grey")   # changes the color of circle
            colorBody=my_elephant.itemcget(elephantbody, 'fill')    # stores the color in a variable
        else: # if they clicked on the wrong shape
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")


def clickTrunk(event):  # function acted out if trunk has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')
        if textElephantFrame == 'Find the 4 Rectangles!': # if text asked user to find rectangles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")
            my_elephant.itemconfig(trunk, fill="grey") # changes color of shape
            colorTrunk=my_elephant.itemcget(trunk, 'fill') # stores color in variable for testing
        else: # if they clicked the wrong shape 
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
        
        if colorEleGrass == 'lawn green' and colorTrunk == 'grey' and colorEleLeftLeg == 'grey' and colorEleRightLeg == 'grey':
            my_elephant.itemconfig(elephanttext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="black")

def clickLeftEye(event):  # function acted out if left eye has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')
        if textElephantFrame == 'Find TEN Circles!': # if text asked user to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")
            my_elephant.itemconfig(lefteye, fill="powder blue") # changes color of shape
            colorEleLeye=my_elephant.itemcget(lefteye, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")


def clickRightEye(event):  # function acted out if right eye has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')
        if textElephantFrame == 'Find TEN Circles!': # if text asked user to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")
            my_elephant.itemconfig(righteye, fill="powder blue") # changes color of shape
            colorEleReye=my_elephant.itemcget(righteye, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")


def clickLeftPupil(event):  # function acted out if left pupil has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')
        if textElephantFrame == 'Find TEN Circles!': # if text asked user to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")
            my_elephant.itemconfig(leftpupil, fill="black") # changes color of shape
            colorEleLP=my_elephant.itemcget(leftpupil, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")


def clickRightPupil(event):  # function acted out if right pupil has been clicked
    global my_elephant
    global colorLeftEar
    global colorRightEar
    global colorEleHead
    global colorEleLeye
    global colorEleReye
    global colorEleRP
    global colorEleLP
    global colorInLear
    global colorInRear
    global colorBody
    global colorTrunk
    global colorEleLeftLeg
    global colorEleRightLeg
    global elephanttext
    global elephantOOPStext
    global colorEleGrass
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorEleGrass != 'lawn green' or colorTrunk != 'grey' or colorLeftEar != 'grey' or colorRightEar != 'grey' or colorEleHead != 'grey' or colorEleLeye != 'powder blue' or colorEleReye != 'powder blue' or colorEleLP != 'black' or colorEleRP != 'black' or colorBody != 'grey' or colorInLear != 'pink' or colorInRear != 'pink' or colorEleLeftLeg != 'grey' or colorEleRightLeg != 'grey':
        textElephantFrame=my_elephant.itemcget(elephanttext, 'text')
        if textElephantFrame == 'Find TEN Circles!': # if text asked user to find circles
            my_elephant.itemconfig(elephantOOPStext, text="Great Job!")
            my_elephant.itemconfig(rightpupil, fill="black") # changes color of shape
            colorEleRP=my_elephant.itemcget(rightpupil, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_elephant.itemconfig(elephantOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftEar == 'grey' and colorRightEar == 'grey' and colorEleHead == 'grey' and colorEleLeye == 'powder blue' and colorEleReye == 'powder blue' and colorEleRP == 'black' and colorEleLP == 'black' and colorBody == 'grey' and colorInLear == 'pink' and colorInRear == 'pink':
            my_elephant.itemconfig(elephanttext, text="Find the 4 Rectangles!", fill="black")



# OWL CLICK FUNCTIONS
# CIRCLES IN OWL
def clickOwlRP(event):  # function acted out if right pupil has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(rightpupil_owl, fill="black") # changes color of shape
            colorRPowl=my_canvas.itemcget(rightpupil_owl, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")


def clickOwlLP(event):  # function acted out if left pupil has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(leftpupil_owl, fill="black") # changes color of shape
            colorLPowl=my_canvas.itemcget(leftpupil_owl, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")


def clickOwlREye(event):  # function acted out if right eye has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlRightEye, fill="powder blue") # changes color of shape
            colorReyeOwl=my_canvas.itemcget(owlRightEye, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")


def clickOwlLEye(event):  # function acted out if left eye has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlLeftEye, fill="powder blue") # changes color of shape
            colorLeyeowl=my_canvas.itemcget(owlLeftEye, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")


def clickOwlHead(event):  # function acted out if head has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlhead, fill="sienna4") # changes color of shape
            colorOwlHead=my_canvas.itemcget(owlhead, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")

def clickOwlBody(event):  # function acted out if body has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlbody, fill="sienna4") # changes color of shape
            colorOwlBody=my_canvas.itemcget(owlbody, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")


def clickOwlStomach(event):  # function acted out if stomach has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the Circles!': # if text asked user to find circles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlstomach, fill="tan4") # changes color of shape
            colorOwlstomach=my_canvas.itemcget(owlstomach, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlstomach == 'tan4' and colorOwlHead == 'sienna4' and colorOwlBody == 'sienna4' and colorLeyeowl == 'powder blue' and colorReyeOwl == 'powder blue' and colorRPowl == 'black' and colorLPowl == 'black':
            my_canvas.itemconfig(owltext, text="Find two Rectangles!", fill="white")

    
# TRIANGLES IN OWL
def clickBeak(event):  # function acted out if beak has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the triangles!': # if text asked user to find triangles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(beak, fill="yellow") # changes color of shape
            colorbeak=my_canvas.itemcget(beak, "fill") # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the triangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorbeak == 'yellow' and colorRear == 'tan4' and colorLear == 'tan4':
            my_canvas.itemconfig(owltext, text="Find all the Circles!", fill="white")
    
 

def clickOwlLEar(event):  # function acted out if left ear has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the triangles!': # if text asked user to find triangles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlleftear, fill="tan4") # changes color of shape
            colorLear=my_canvas.itemcget(owlleftear, "fill") # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the triangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorbeak == 'yellow' and colorRear == 'tan4' and colorLear == 'tan4':
            my_canvas.itemconfig(owltext, text="Find all the Circles!", fill="white")


def clickOwlREar(event):  # function acted out if right ear has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find all the triangles!': # if text asked user to find triangles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(owlrightear, fill="tan4") # changes color of shape
            colorRear=my_canvas.itemcget(owlrightear, "fill") # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the triangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorbeak == 'yellow' and colorRear == 'tan4' and colorLear == 'tan4':
            my_canvas.itemconfig(owltext, text="Find all the Circles!", fill="white")

    
# RECTANGLES IN OWL
def clickRightFoot(event):  # function acted out if right foot has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find two Rectangles!': # if text asked user to find rectangles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(rightfoot, fill="yellow") # changes color of shape
            colorOwlRleg=my_canvas.itemcget(rightfoot, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlLleg == 'yellow' and colorOwlRleg == 'yellow':
            my_canvas.itemconfig(owltext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="white")


def clickLeftFoot(event):  # function acted out if left foot has been clicked
    global owltext
    global owlOOPStext
    global colorbeak
    global colorLear
    global colorRear
    global colorRPowl
    global colorLPowl
    global colorReyeOwl
    global colorLeyeowl
    global colorOwlBody
    global colorOwlstomach
    global colorOwlHead
    global colorOwlLleg
    global colorOwlRleg
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorbeak != 'yellow' or colorLear != 'tan4' or colorRear != 'tan4' or colorRPowl != 'black' or colorLPowl != 'black' or colorReyeOwl != 'powder blue' or colorLeyeowl != 'powder blue' or colorOwlBody != 'sienna4' or colorOwlstomach != 'tan4' or colorOwlHead != 'sienna4' or colorOwlLleg != 'yellow' or colorOwlRleg != 'yellow':
        textOwlFrame=my_canvas.itemcget(owltext, 'text')
    
        if textOwlFrame == 'Find two Rectangles!': # if text asked user to find rectangles
            my_canvas.itemconfig(owlOOPStext, text="Great Job!")
            my_canvas.itemconfig(leftfoot, fill="yellow") # changes color of shape
            colorOwlLleg=my_canvas.itemcget(leftfoot, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_canvas.itemconfig(owlOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOwlLleg == 'yellow' and colorOwlRleg == 'yellow':
            my_canvas.itemconfig(owltext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="white")






# HOUSE CLICK FUNCTIONS
def clickGrass(event):  # function acted out if grass has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 3 Rectangles!': # if text asked user to find rectangles
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(grass, fill="green") # changes color of shape
            colorGrass=my_house.itemcget(grass, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorDoor == 'brown' and colorGrass == 'green' and colorHouse == 'red':
            my_house.itemconfig(housetext, text='Find the 2 Circles!')

def clickHouse(event):  # function acted out if house has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 3 Rectangles!': # if text asked user to find rectangles
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(house, fill="red") # changes color of shape
            colorHouse=my_house.itemcget(house, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorDoor == 'brown' and colorGrass == 'green' and colorHouse == 'red':
            my_house.itemconfig(housetext, text='Find the 2 Circles!')

def clickRoof(event):  # function acted out if roof has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the Triangle!': # if text asked user to find triangle
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(roof, fill="sienna4") # changes color of shape
            colorRoof=my_house.itemcget(roof, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the triangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorRoof == 'sienna4':
            my_house.itemconfig(housetext, text='Find the 3 Rectangles!')

def clickDoor(event):  # function acted out if door has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 3 Rectangles!': # if text asked user to find rectangles
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(door, fill="brown") # changes color of shape
            colorDoor=my_house.itemcget(door, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorDoor == 'brown' and colorGrass == 'green' and colorHouse == 'red':
            my_house.itemconfig(housetext, text='Find the 2 Circles!')

def clickHandle(event):  # function acted out if handle has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 2 Circles!': # if text asked user to find circles
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(handle, fill="black") # changes color of shape
            colorHandle=my_house.itemcget(handle, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorHandle == 'black' and colorSun == 'yellow':
            my_house.itemconfig(housetext, text='Find the 2 squares!')

def clickWindowLeft(event):  # function acted out if left window has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 2 squares!': # if text asked user to find squares
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(windowLeft, fill="powder blue") # changes color of shape
            colorLeftWin=my_house.itemcget(windowLeft, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the squares in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftWin == 'powder blue' and colorRightWin == 'powder blue':
            my_house.itemconfig(housetext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="black")

def clickWindowRight(event):  # function acted out if right window has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 2 squares!': # if text asked user to find squares
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(windowRight, fill="powder blue") # changes color of shape
            colorRightWin=my_house.itemcget(windowRight, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the squares in the picture have been clicked (colorized), if they have, instruction text changes
        if colorLeftWin == 'powder blue' and colorRightWin == 'powder blue':
            my_house.itemconfig(housetext, text="YAY! You found all the shapes!", font=('Ink Free', 15, 'bold'), fill="black")

def clickSun(event):  # function acted out if sun has been clicked
    global colorGrass
    global colorHouse
    global colorDoor
    global colorHandle
    global colorRoof
    global colorSun
    global colorLeftWin
    global colorRightWin
    global housetext
    global houseOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorGrass != 'green' or colorHouse != 'red' or colorDoor != 'brown' or colorRoof != 'sienna4' or colorHandle != 'black' or colorSun != 'yellow' or colorLeftWin != 'powder blue' or colorRightWin != 'powder blue':
        textHouseFrame=my_house.itemcget(housetext, 'text')
    
        if textHouseFrame == 'Find the 2 Circles!': # if text asked user to find circles
            my_house.itemconfig(houseOOPStext, text="Great Job!")
            my_house.itemconfig(sun, fill="yellow") # changes color of shape
            colorSun=my_house.itemcget(sun, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_house.itemconfig(houseOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorHandle == 'black' and colorSun == 'yellow':
            my_house.itemconfig(housetext, text='Find the 2 squares!')

    





# TRAIN CLICK FUNCTIONS
def clickVertBody(event):  # function acted out if vert body has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find 6 Rectangles!':  # if text asked user to find rectangles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(vertBody, fill="blue") # changes color of shape
            colorVertBody=my_train.itemcget(vertBody, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorVertBody == 'blue' and colorWindow == 'yellow' and colorHorBody == 'blue' and colorWheelBar == 'grey' and colorChimneyBase == 'blue' and colorChimney == 'black':
            my_train.itemconfig(traintext, text='Find the 4 Circles!')

def clickWindow(event):  # function acted out if window has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find 6 Rectangles!':  # if text asked user to find rectangles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(window, fill="yellow") # changes color of shape
            colorWindow=my_train.itemcget(window, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorVertBody == 'blue' and colorWindow == 'yellow' and colorHorBody == 'blue' and colorWheelBar == 'grey' and colorChimneyBase == 'blue' and colorChimney == 'black':
            my_train.itemconfig(traintext, text='Find the 4 Circles!')



def clickOutWheel(event):  # function acted out if outer wheel has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find the 4 Circles!':  # if text asked user to find circles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(outwheel, fill="black") # changes color of shape
            colorOutWheel=my_train.itemcget(outwheel, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOutWheel == 'black' and colorInnerWheel == 'grey' and colorFrontWheel == 'black' and colorMiddleWheel == 'black':
            my_train.itemconfig(traintext, text='YAY! You found all the shapes!', font=('Ink Free', 15, 'bold'), fill="white")

def clickInnerWheel(event):  # function acted out if inner wheel has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find the 4 Circles!':  # if text asked user to find circles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(innerwheel, fill="grey") # changes color of shape
            colorInnerWheel=my_train.itemcget(innerwheel, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOutWheel == 'black' and colorInnerWheel == 'grey' and colorFrontWheel == 'black' and colorMiddleWheel == 'black':
            my_train.itemconfig(traintext, text='YAY! You found all the shapes!', font=('Ink Free', 15, 10, 'bold'), fill="white")

def clickHorBody(event):  # function acted out if horizontal body has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find 6 Rectangles!':  # if text asked user to find rectangles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(horBody, fill="blue") # changes color of shape
            colorHorBody=my_train.itemcget(horBody, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorVertBody == 'blue' and colorWindow == 'yellow' and colorHorBody == 'blue' and colorWheelBar == 'grey' and colorChimneyBase == 'blue' and colorChimney == 'black':
            my_train.itemconfig(traintext, text='Find the 4 Circles!')

def clickTriangle(event):  # function acted out if triangle has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find the Triangle!': # if text asked user to find triangle
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(triangle, fill="blue") # changes color of shape
            colorTriangle=my_train.itemcget(triangle, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the triangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorTriangle == 'blue':
            my_train.itemconfig(traintext, text='Find 6 Rectangles!')

def clickMiddleWheel(event):  # function acted out if middle wheel has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find the 4 Circles!':  # if text asked user to find circles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(middlewheel, fill="black") # changes color of shape
            colorMiddleWheel=my_train.itemcget(middlewheel, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOutWheel == 'black' and colorInnerWheel == 'grey' and colorFrontWheel == 'black' and colorMiddleWheel == 'black':
            my_train.itemconfig(traintext, text='YAY! You found all the shapes!', font=('Ink Free', 15, 'bold'), fill="white")

def clickFrontWheel(event):  # function acted out if front wheel has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find the 4 Circles!':  # if text asked user to find circles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(frontwheel, fill="black") # changes color of shape
            colorFrontWheel=my_train.itemcget(frontwheel, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the circles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorOutWheel == 'black' and colorInnerWheel == 'grey' and colorFrontWheel == 'black' and colorMiddleWheel == 'black':
            my_train.itemconfig(traintext, text='YAY! You found all the shapes!', font=('Ink Free', 15, 'bold'), fill="white")

def clickWheelBar(event):  # function acted out if wheel bar has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find 6 Rectangles!': # if text asked user to find rectangles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(wheelbar, fill="grey") # changes color of shape
            colorWheelBar=my_train.itemcget(wheelbar, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorVertBody == 'blue' and colorWindow == 'yellow' and colorHorBody == 'blue' and colorWheelBar == 'grey' and colorChimneyBase == 'blue' and colorChimney == 'black':
            my_train.itemconfig(traintext, text='Find the 4 Circles!')
    

def clickChimneyBase(event):  # function acted out if chimney base has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find 6 Rectangles!':  # if text asked user to find rectangles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(chimneybase, fill="blue") # changes color of shape
            colorChimneyBase=my_train.itemcget(chimneybase, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorVertBody == 'blue' and colorWindow == 'yellow' and colorHorBody == 'blue' and colorWheelBar == 'grey' and colorChimneyBase == 'blue' and colorChimney == 'black':
            my_train.itemconfig(traintext, text='Find the 4 Circles!')

def clickChimney(event):  # function acted out if chimney has been clicked
    global traintext
    global colorWheelBar
    global colorChimneyBase
    global colorChimney
    global colorHorBody
    global colorVertBody
    global colorTriangle
    global colorInnerWheel
    global colorOutWheel
    global colorMiddleWheel
    global colorWindow
    global colorFrontWheel
    global trainOOPStext
# IF STATEMENT TO CHECK IF PICTURE IS FULLY COLORED, IF ITS NOT, PROCEED
    if colorWindow != 'yellow' or colorWheelBar != 'grey' or colorChimneyBase != 'blue' or colorChimney != 'black' or colorHorBody != 'blue' or colorVertBody != 'blue' or colorTriangle != 'blue' or colorInnerWheel != 'grey' or colorOutWheel != 'black' or colorMiddleWheel != 'black' or colorFrontWheel != 'black':
        textTrainFrame=my_train.itemcget(traintext, 'text')
        if textTrainFrame == 'Find 6 Rectangles!':  # if text asked user to find rectangles
            my_train.itemconfig(trainOOPStext, text="Great Job!")
            my_train.itemconfig(chimney, fill="black") # changes color of shape
            colorChimney=my_train.itemcget(chimney, 'fill') # stores color in variable for testing
        else: # if they clicked on the wrong shape
            my_train.itemconfig(trainOOPStext, text="OOPS! Try Again!")
# checks if all the rectangles in the picture have been clicked (colorized), if they have, instruction text changes
        if colorVertBody == 'blue' and colorWindow == 'yellow' and colorHorBody == 'blue' and colorWheelBar == 'grey' and colorChimneyBase == 'blue' and colorChimney == 'black':
            my_train.itemconfig(traintext, text='Find the 4 Circles!')




##### COLOR GAME CLICK FUNCTION DECLARATIONS #####
def clickYellowSquare(event):  # function acted out if yellow square has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'YELLOW shapes':  # if directions asks for yellow shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(squareYellow, fill='black')   # colors shape black
            colorYellowSquare = colorCanvas.itemcget(squareYellow, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorYellowCircle == 'black' and colorYellowSquare == 'black':   # if all yellow shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='BLUE shapes', fill='blue')
    
    
def clickBlueRect(event):  # function acted out if blue rect has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'BLUE shapes':  # if directions asks for BLUE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(blueRect, fill='black')   # colors shape black
            colorBlueRect = colorCanvas.itemcget(blueRect, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorBlueRect == 'black' and colorBlueSquare == 'black' and colorBlueOval == 'black' and colorBlueTriangle == 'black':   # if all blue shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='GREEN shapes', fill='lime green')
        
def clickPurpleOval(event):  # function acted out if purple oval has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'PURPLE shapes':  # if directions asks for PURPLE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(ovalPurple, fill='black')   # colors shape black
            colorPurpleOval = colorCanvas.itemcget(ovalPurple, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorPurpleOval == 'black' and colorPurpleRect == 'black':   # if all purple shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='ORANGE shapes', fill='dark orange')

    
def clickBlueTri(event):  # function acted out if blue triangle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'BLUE shapes':  # if directions asks for BLUE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(triangleBlue, fill='black')   # colors shape black
            colorBlueTriangle = colorCanvas.itemcget(triangleBlue, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorBlueRect == 'black' and colorBlueSquare == 'black' and colorBlueOval == 'black' and colorBlueTriangle == 'black':   # if all blue shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='GREEN shapes', fill='lime green')

def clickGreenTri(event):  # function acted out if green triangle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'GREEN shapes':  # if directions asks for GREEN shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(triGreen, fill='black')   # colors shape black
            colorGreenTriangle = colorCanvas.itemcget(triGreen, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorGreenTriangle == 'black' and colorGreenRect == 'black':   # if all green shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='PURPLE shapes', fill='purple')

def clickRedCircle(event):  # function acted out if red circle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'RED shapes':  # if directions asks for RED shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(redCircle, fill='black')   # colors shape black
            colorRedCircle = colorCanvas.itemcget(redCircle, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorRedCircle == 'black' and colorRedRect == 'black' and colorRedOval == 'black':   # if all red shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='YELLOW shapes', fill='yellow')
        
def clickOrangeCircle(event):  # function acted out if orange circle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'ORANGE shapes':  # if directions asks for ORANGE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(circleOrange, fill='black')   # colors shape black
            colorOrangeCircle = colorCanvas.itemcget(circleOrange, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorOrangeTri == 'black' and colorOrangeCircle == 'black':   # if all orange shapes have been clicked
            colorCanvas.itemconfig(colorText, text='CONGRATULATIONS!', font=('Kristen ITC', 25, 'bold'), fill='white')
            colorCanvas.itemconfig(colorText1, text='You found all the colors!', font=('Kristen ITC', 20, 'bold'), fill='white')
        
def clickGreenRect(event):  # function acted out if green rectangle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'GREEN shapes':  # if directions asks for GREEN shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(rectGreen, fill='black')   # colors shape black
            colorGreenRect = colorCanvas.itemcget(rectGreen, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorGreenTriangle == 'black' and colorGreenRect == 'black':   # if all green shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='PURPLE shapes', fill='purple')
        
def clickRedRect(event):  # function acted out if red rectangle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'RED shapes':  # if directions asks for RED shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(rectRed, fill='black')   # colors shape black
            colorRedRect = colorCanvas.itemcget(rectRed, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorRedCircle == 'black' and colorRedRect == 'black' and colorRedOval == 'black':   # if all red shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='YELLOW shapes', fill='yellow')
        
def clickPurpleRect(event):  # function acted out if purple rectangle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'PURPLE shapes':  # if directions asks for PURPLE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(purpleRect, fill='black')   # colors shape black
            colorPurpleRect = colorCanvas.itemcget(purpleRect, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorPurpleOval == 'black' and colorPurpleRect == 'black':   # if all purple shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='ORANGE shapes', fill='dark orange')
        
def clickBlueSquare(event):  # function acted out if blue sqaure has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'BLUE shapes':  # if directions asks for BLUE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(squareBlue, fill='black')   # colors shape black
            colorBlueSquare = colorCanvas.itemcget(squareBlue, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorBlueRect == 'black' and colorBlueSquare == 'black' and colorBlueOval == 'black' and colorBlueTriangle == 'black':   # if all blue shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='GREEN shapes', fill='lime green')

def clickOrangeTri(event):  # function acted out if orange triangle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'ORANGE shapes':  # if directions asks for ORANGE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(orangeTri, fill='black')   # colors shape black
            colorOrangeTri = colorCanvas.itemcget(orangeTri, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorOrangeTri == 'black' and colorOrangeCircle == 'black':   # if all orange shapes have been clicked
            colorCanvas.itemconfig(colorText, text='CONGRATULATIONS!', font=('Kristen ITC', 25, 'bold'), fill='white')
            colorCanvas.itemconfig(colorText1, text='You found all the colors!', font=('Kristen ITC', 20, 'bold'), fill='white')

def clickBlueOval(event):  # function acted out if blue oval has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'BLUE shapes':  # if directions asks for BLUE shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(blueOval, fill='black')   # colors shape black
            colorBlueOval = colorCanvas.itemcget(blueOval, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorBlueRect == 'black' and colorBlueSquare == 'black' and colorBlueOval == 'black' and colorBlueTriangle == 'black':   # if all blue shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='GREEN shapes', fill='lime green')

def clickYellowCircle(event):  # function acted out if yellow circle has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'YELLOW shapes':  # if directions asks for yellow shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(circleYellow, fill='black')   # colors shape black
            colorYellowCircle = colorCanvas.itemcget(circleYellow, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorYellowCircle == 'black' and colorYellowSquare == 'black':   # if all yellow shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='BLUE shapes', fill='blue')

def clickRedOval(event):  # function acted out if red oval has been clicked
    global colorText
    global colorText1
    global colorYellowCircle
    global colorYellowSquare
    global colorRedCircle
    global colorRedOval
    global colorRedRect
    global colorBlueOval
    global colorBlueRect
    global colorBlueSquare
    global colorBlueTriangle
    global colorOrangeCircle
    global colorOrangeTri
    global colorGreenRect
    global colorGreenTriangle
    global colorPurpleOval
    global colorPurpleRect
    global colorOOPStext
# if all the shapes have not been found, proceed
    if colorYellowCircle != 'black' or colorYellowSquare != 'black'  or colorRedCircle != 'black' or colorRedOval != 'black' or colorRedRect != 'black' or colorBlueOval != 'black' or colorBlueRect != 'black' or colorBlueSquare != 'black' or colorBlueTriangle != 'black' or colorOrangeCircle != 'black' or colorOrangeTri != 'black' or colorGreenRect != 'black' or colorGreenTriangle != 'black' or colorPurpleOval != 'black' or colorPurpleRect != 'black':
        colorToFind=colorCanvas.itemcget(colorText1, 'text')    # pull text from directions
        if colorToFind == 'RED shapes':  # if directions asks for RED shape
            colorCanvas.itemconfig(colorOOPStext, text='Great Job!')
            colorCanvas.itemconfig(ovalRed, fill='black')   # colors shape black
            colorRedOval = colorCanvas.itemcget(ovalRed, 'fill') # pulls current color from shape to store in variable
        else: # if they clicked on a wrong color shape
            colorCanvas.itemconfig(colorOOPStext, text="OOPS! Try Again!")
        
        if colorRedCircle == 'black' and colorRedRect == 'black' and colorRedOval == 'black':   # if all red shapes have been clicked
            colorCanvas.itemconfig(colorText1, text='YELLOW shapes', fill='yellow')



# DECLARATION SECTION/INITIALIZATION OF ALL SCREENS AND SHAPES/GRAPHICS

root = tk.Tk()
root.title('Color Me Shapes')
root.geometry("500x540")

first_screen = tk.Frame(root)       # creates first welcome screen
main_frame = tk.Frame(root)         # creates picture main menu screen
color_frame = tk.Frame(root)        # creates color screen
number_frame = tk.Frame(root)       # creates number screen
owl_frame = tk.Frame(root)          # creates owl screen
elephant_frame=tk.Frame(root)       # creates elephant screen
house_frame = tk.Frame(root)        # creates house screen
train_frame = tk.Frame(root)        # creates train screen


##### COLOR GAME SCREEN #####
#   -creates all the text and shapes on the screen and initializes all shapes to starting color
#   -turns all shapes into buttons by binding actions to them to change the color of the shape
#     once it has been clicked, the action bound to each shape is the left mouse click
#   -initializes the directions block and text(dirBlock, colorText1, colorText2), 
#     which tells the user what color to look for
#   -initializes a message (colorOOPStext) which lets user know if they clicked the right color shape
colorCanvas = Canvas(color_frame, width=490, height=450, bg="black") # creates canvas on color game
colorCanvas.pack(pady=20)
dirBlock = colorCanvas.create_rectangle(15, 10, 475, 120, fill="grey23")
colorText = colorCanvas.create_text(245, 40, text="Find all the", font=('Kristen ITC', 40, 'bold'), justify = 'center', fill='white')
colorText1 = colorCanvas.create_text(245, 90, text="RED shapes", font=('Kristen ITC', 40, 'bold'), justify = 'center', fill='red')
colorOOPStext = colorCanvas.create_text(245, 420, text=" ", font=('Ink Free', 20, 'bold'), justify = 'center', fill='white')
squareYellow = colorCanvas.create_rectangle(50, 130, 100, 175, fill="yellow")
colorCanvas.tag_bind(squareYellow, '<Button-1>', clickYellowSquare)
circleYellow = colorCanvas.create_oval(400, 360, 450, 410, fill="yellow")
colorCanvas.tag_bind(circleYellow, '<Button-1>', clickYellowCircle)
rectGreen = colorCanvas.create_rectangle(280, 250, 320, 330, fill="lime green")
colorCanvas.tag_bind(rectGreen, '<Button-1>', clickGreenRect)
ovalRed = colorCanvas.create_oval(50, 350, 130, 400, fill='red')
colorCanvas.tag_bind(ovalRed, '<Button-1>', clickRedOval)
triangleBlue = colorCanvas.create_polygon(400, 190, 430, 130, 460, 190, fill='blue')
colorCanvas.tag_bind(triangleBlue, '<Button-1>', clickBlueTri)
circleOrange = colorCanvas.create_oval(200, 230, 260, 290, fill='dark orange')
colorCanvas.tag_bind(circleOrange, '<Button-1>', clickOrangeCircle)
ovalPurple = colorCanvas.create_oval(245, 140, 375, 210, fill='purple')
colorCanvas.tag_bind(ovalPurple, '<Button-1>', clickPurpleOval)
squareBlue= colorCanvas.create_rectangle(150, 310, 240, 400, fill='blue')
colorCanvas.tag_bind(squareBlue, '<Button-1>', clickBlueSquare)
rectRed = colorCanvas.create_rectangle(340, 220, 450, 280, fill='red')
colorCanvas.tag_bind(rectRed, '<Button-1>', clickRedRect)
triGreen = colorCanvas.create_polygon(40, 200, 120, 200, 80, 280, fill='lime green') 
colorCanvas.tag_bind(triGreen, '<Button-1>', clickGreenTri)
blueRect = colorCanvas.create_rectangle(130, 140, 225, 200, fill='blue')
colorCanvas.tag_bind(blueRect, '<Button-1>', clickBlueRect)
redCircle = colorCanvas.create_oval(120, 210, 190, 280, fill='red')
colorCanvas.tag_bind(redCircle, '<Button-1>', clickRedCircle)
purpleRect = colorCanvas.create_rectangle(40, 300, 130, 340, fill='purple')
colorCanvas.tag_bind(purpleRect, '<Button-1>', clickPurpleRect)
orangeTri = colorCanvas.create_polygon(260, 355, 390, 355, 325, 400, fill='dark orange')
colorCanvas.tag_bind(orangeTri, '<Button-1>', clickOrangeTri)
blueOval = colorCanvas.create_oval(340, 300, 450, 340, fill='blue')
colorCanvas.tag_bind(blueOval, '<Button-1>', clickBlueOval)

# button to quit from color frame
color_quit = tk.Button(color_frame, text = 'Quit', command = root.destroy)
color_quit.pack(side=BOTTOM)
# button to go back to first screen from color game
load_first_color = tk.Button(color_frame, text = 'Main Menu', command = show_first_C)
load_first_color.pack(side = BOTTOM)





#### NUMBERS AND COUNTING FRAME ####
#   -declares and initializes directions text (numDirText) and directions block (numDirBlock)
#   -creates a number panel 1-5 at bottom of canvas where each # is bound to actions by a left click of the mouse
#   -initializes and creates first set of shapes (two circles) and initializes the beginning text
#     asking the user 'how many circles do you see?'
#   -initializes a message (numOOPStext) which lets user know if they clicked the right number
numberCanvas = Canvas(number_frame, width=490, height=470, bg="maroon") # Canvas for counting game
numberCanvas.pack(pady=5)
numDirBlock = numberCanvas.create_rectangle(20, 20, 470, 80, fill='pale violet red')
numDirText = numberCanvas.create_text(245, 50, text="How many Circles do you see?", font=('Comic Sans MS', 20, 'bold'), justify='center', fill='white')
numOOPSText = numberCanvas.create_text(245, 360, text=" ", font=('Comic Sans MS', 20, 'bold'), justify='center', fill='white')
numOneBox = numberCanvas.create_rectangle(22, 380, 112, 470, fill='violet red')
numberCanvas.tag_bind(numOneBox, '<Button-1>', numOneClicked)
numOne = numberCanvas.create_text(67, 425, text='1', font=('Impact', 40), fill='white')
numberCanvas.tag_bind(numOne, '<Button-1>', numOneClicked)
numTwoBox = numberCanvas.create_rectangle(112, 380, 202, 470, fill='dark orange')
numberCanvas.tag_bind(numTwoBox, '<Button-1>', numTwoClicked)
numTwo = numberCanvas.create_text(157, 425, text='2', font=('Impact', 40), fill='white')
numberCanvas.tag_bind(numTwo, '<Button-1>', numTwoClicked)
numThreeBox = numberCanvas.create_rectangle(202, 380, 292, 470, fill='gold')
numberCanvas.tag_bind(numThreeBox, '<Button-1>', numThreeClicked)
numThree = numberCanvas.create_text(247, 425, text='3', font=('Impact', 40), fill='white')
numberCanvas.tag_bind(numThree, '<Button-1>', numThreeClicked)
numFourBox = numberCanvas.create_rectangle(292, 380, 382, 470, fill='green yellow')
numberCanvas.tag_bind(numFourBox, '<Button-1>', numFourClicked)
numFour = numberCanvas.create_text(337, 425, text='4', font=('Impact', 40), fill='white')
numberCanvas.tag_bind(numFour, '<Button-1>', numFourClicked)
numFiveBox = numberCanvas.create_rectangle(382, 380, 472, 470, fill='lime green')
numberCanvas.tag_bind(numFiveBox, '<Button-1>', numFiveClicked)
numFive = numberCanvas.create_text(427, 425, text='5', font=('Impact', 40), fill='white')
numberCanvas.tag_bind(numFive, '<Button-1>', numFiveClicked)

# Beginning Shapes on Canvas for Number Game
twoCircles1 = numberCanvas.create_oval(50, 155, 230, 335, fill='lime green')
twoCircles2 = numberCanvas.create_oval(260, 155, 440, 335, fill='lime green')
# button to quit from number frame
num_quit = tk.Button(number_frame, text = 'Quit', command = root.destroy)
num_quit.pack(side=BOTTOM)
# button to go back to first screen from color game
load_first_num = tk.Button(number_frame, text = 'Main Menu', command = show_firstNum)
load_first_num.pack(side = BOTTOM)



###### WELCOME SCREEN ######
#   -creates a colorful canvas welcoming user
#   -declares and initializes a direction block and directions telling the user what each game does
#   -creates a line of shapes to make screen fun and bright looking
#   -creates three ovals with text inside which are each bound to an action by the left click of the mouse
#   -the action sends the user to whatever game their button is for
welcomeCanvas = Canvas(first_screen, width=490, height=520, bg="light sky blue")
welcomeCanvas.pack(pady=1)
welcomeText = welcomeCanvas.create_text(245, 60, text="Color Me Shapes", font=('Kristen ITC', 40, 'bold'), justify = 'center', fill='black')
miniSquare = welcomeCanvas.create_rectangle(50, 105, 100, 155, fill="orchid3")
miniOval = welcomeCanvas.create_oval(120, 105, 200, 155, fill="pink")
miniTri = welcomeCanvas.create_polygon(220, 155, 245, 105, 270, 155, fill="orange", outline="black")
miniRect = welcomeCanvas.create_rectangle(290, 105, 370, 155, fill="yellow")
miniCircle = welcomeCanvas.create_oval(390, 105, 440, 155, fill="green yellow")
directionsBlock = welcomeCanvas.create_rectangle(20, 165, 470, 240, fill="pale green")
directionsLine1 = welcomeCanvas.create_text(245, 180, text="To learn shapes and color a Masterpiece, click Color Shapes!", font=('Comic Sans MS', 12), justify = 'center', fill='black')
directionsLine2 = welcomeCanvas.create_text(245, 200, text="To play Where's the Color, click Learn Colors!", font=('Comic Sans MS', 12), justify = 'center', fill='black')
directionsLine3 = welcomeCanvas.create_text(245, 220, text="To practice numbers and counting up to 5, click Counting!", font=('Comic Sans MS', 12), justify = 'center', fill='black')
playGame = welcomeCanvas.create_oval(100, 250, 390, 330, fill="orchid1")
welcomeCanvas.tag_bind(playGame, '<Button-1>', show_mainframe)
playGameText = welcomeCanvas.create_text(245, 290, text="Color Shapes", font=('Impact', 30), justify = 'center', fill='black')
welcomeCanvas.tag_bind(playGameText, '<Button-1>', show_mainframe)
colorGame = welcomeCanvas.create_oval(100, 340, 390, 420, fill='blue violet')
welcomeCanvas.tag_bind(colorGame, '<Button-1>', show_colorFrame)
colorGameText = welcomeCanvas.create_text(245, 380, text="Learn Colors", font=('Impact', 30), justify = 'center', fill='black')
welcomeCanvas.tag_bind(colorGameText, '<Button-1>', show_colorFrame)
numButton = welcomeCanvas.create_oval(100, 430, 390, 510, fill='Slateblue1')
welcomeCanvas.tag_bind(numButton, '<Button-1>', show_numFrame)
numButtonText = welcomeCanvas.create_text(245, 470, text="Counting", font=('Impact', 30), justify = 'center', fill='black')
welcomeCanvas.tag_bind(numButtonText, '<Button-1>', show_numFrame)


###### BUTTONS FOR PICTURE MENU SCREEN ######
#   -creates four ovals with text inside which become "buttons" by being bound to an action
#   -the action on each "button" leads the user to the picture they chose
#   -creates text at top of screen asking user to pick a picture and click on the button associated to that picture
mainCanvas = Canvas(main_frame, width=490, height=410, bg="orchid3")
mainCanvas.pack(pady=20)
mainMenuDirBlock = mainCanvas.create_rectangle(20, 15, 470, 65, fill='pale green')
mainText = mainCanvas.create_text(245, 28, text="Pick a picture to find all the shapes", font=('Comic Sans MS', 15, 'bold'), justify = 'center', fill='black')
mainText1 = mainCanvas.create_text(245, 50, text="and color your Masterpiece!", font=('Comic Sans MS', 15, 'bold'), justify = 'center', fill='black')
pickOwl = mainCanvas.create_oval(110, 80, 380, 140, fill="medium violet red")
mainCanvas.tag_bind(pickOwl, '<Button-1>', show_owl)
pickOwlText = mainCanvas.create_text(245, 110, text="Owl", font=('Kristen ITC', 25, 'bold'), justify = 'center', fill='black')
mainCanvas.tag_bind(pickOwlText, '<Button-1>', show_owl)
pickElephant = mainCanvas.create_oval(110, 160, 380, 220, fill="blue violet")
mainCanvas.tag_bind(pickElephant, '<Button-1>', show_elephant)
pickElephantText = mainCanvas.create_text(245, 190, text="Elephant", font=('Kristen ITC', 25, 'bold'), justify = 'center', fill='black')
mainCanvas.tag_bind(pickElephantText, '<Button-1>', show_elephant)
pickHouse = mainCanvas.create_oval(110, 240, 380, 300, fill="dodger blue")
mainCanvas.tag_bind(pickHouse, '<Button-1>', show_house)
pickHouseText = mainCanvas.create_text(245, 270, text="House", font=('Kristen ITC', 25, 'bold'), justify = 'center', fill='black')
mainCanvas.tag_bind(pickHouseText, '<Button-1>', show_house)
pickTrain = mainCanvas.create_oval(110, 320, 380, 380, fill="spring green")
mainCanvas.tag_bind(pickTrain, '<Button-1>', show_train)
pickTrainText = mainCanvas.create_text(245, 350, text="Train", font=('Kristen ITC', 25, 'bold'), justify = 'center', fill='black')
mainCanvas.tag_bind(pickTrainText, '<Button-1>', show_train)

#button to quit from picture menu
load_main_exit = tk.Button(main_frame, text = 'Quit', command = root.destroy)
load_main_exit.pack(side=BOTTOM)
# button to go back to welcome screen from picture menu
load_first_main = tk.Button(main_frame, text = 'Main Menu', command = show_main_F)
load_first_main.pack(side = BOTTOM)

#button to go back to main from owl
load_main_owl = tk.Button(owl_frame, text = 'Picture Menu', command = show_main_O)
load_main_owl.pack(side = BOTTOM)

#button to go back to main from elephant
load_main_elephant = tk.Button(elephant_frame, text = 'Picture Menu', command = show_main_E)
load_main_elephant.pack(side = BOTTOM)

#button to go back to main from house
load_main_house = tk.Button(house_frame, text = 'Picture Menu', command = show_main_H)
load_main_house.pack(side = BOTTOM)

#button to go back to main from train
load_main_train = tk.Button(train_frame, text = 'Picture Menu', command = show_main_T)
load_main_train.pack(side = BOTTOM)



#### OWL DRAWING ####
#   -creates a picture of an owl out of shapes using the create_oval, create_polygon and create_rectangle functions
#   -the owl drawing's shapes are all initialized to white so the picture is not colorized
#   -each shape is bound to an action and function which changes the color of the shape if the user
#     clicked on the correct shape
#   -owlOOPStext is initialized and will change depending on if the user clicks on the correct or wrong shapes
#   -owltext is initialized to ask user to find all the triangles in the owl drawing
my_canvas = Canvas(owl_frame, width=300, height=450, bg="midnight blue")
my_canvas.pack(pady=20)
owlOOPStext = my_canvas.create_text(150, 410, text=" ", font=('Ink Free', 20, 'bold'), justify = 'center', fill='white')
owltext = my_canvas.create_text(150, 20, text="Find all the triangles!", font=('Kristen ITC', 20, 'bold'), justify = 'center', fill='white')
owlhead = my_canvas.create_oval(50, 250, 250, 50, fill="white")
my_canvas.tag_bind(owlhead, '<Button-1>', clickOwlHead)
owlLeftEye = my_canvas.create_oval(100, 100, 150, 150, fill="white")
my_canvas.tag_bind(owlLeftEye, '<Button-1>', clickOwlLEye)
owlRightEye = my_canvas.create_oval(150, 100, 200, 150, fill="white")
my_canvas.tag_bind(owlRightEye, '<Button-1>', clickOwlREye)
beak = my_canvas.create_polygon(125, 150, 175, 150, 150, 200, fill="white", outline="black")
my_canvas.tag_bind(beak, '<Button-1>', clickBeak)
owlleftear = my_canvas.create_polygon(65, 100, 130, 50, 65, 50, fill="white", outline="black")
my_canvas.tag_bind(owlleftear, '<Button-1>', clickOwlLEar)
owlrightear = my_canvas.create_polygon(235, 100, 170, 50, 235, 50, fill="white", outline="black")
my_canvas.tag_bind(owlrightear, '<Button-1>', clickOwlREar)
leftpupil_owl = my_canvas.create_oval(120, 120, 130, 130, fill="white")
my_canvas.tag_bind(leftpupil_owl, '<Button-1>', clickOwlLP)
rightpupil_owl = my_canvas.create_oval(170, 120, 180, 130, fill="white")
my_canvas.tag_bind(rightpupil_owl, '<Button-1>', clickOwlRP)
leftfoot = my_canvas.create_rectangle(110, 390, 120, 360, fill="white")
my_canvas.tag_bind(leftfoot, '<Button-1>', clickLeftFoot)
rightfoot = my_canvas.create_rectangle(180, 390, 190, 360, fill="white")
my_canvas.tag_bind(rightfoot, '<Button-1>', clickRightFoot)
owlbody = my_canvas.create_oval(75, 375, 225, 250, fill="white")
my_canvas.tag_bind(owlbody, '<Button-1>', clickOwlBody)
owlstomach = my_canvas.create_oval(110, 350, 190, 275, fill="white")
my_canvas.tag_bind(owlstomach, '<Button-1>', clickOwlStomach)

# HOUSE DRAWING
#   -creates a picture of an house out of shapes using the create_oval, create_polygon and create_rectangle functions
#   -the house drawing's shapes are all initialized to white so the picture is not colorized
#   -each shape is bound to an action and function which changes the color of the shape if the user
#     clicked on the correct shape
#   -houseOOPStext is initialized and will change depending on if the user clicks on the correct or wrong shapes
#   -housetext is initialized to ask user to find all the triangles in the house drawing
my_house= Canvas(house_frame, width=300, height=400, bg="cyan") # canvas for house drawing
my_house.pack(pady=20)
houseOOPStext = my_house.create_text(170, 50, text=" ", font=('Kristen ITC', 10, 'bold'), justify = 'center', fill='black')
housetext = my_house.create_text(150, 20, text="Find the Triangle!", font=('Kristen ITC', 18, 'bold'), justify = 'center', fill='black')
grass = my_house.create_rectangle(0, 400, 300, 350, fill="white")
my_house.tag_bind(grass, '<Button-1>', clickGrass)
house = my_house.create_rectangle(80, 350, 220, 200, fill="white")
my_house.tag_bind(house, '<Button-1>', clickHouse)
roof = my_house.create_polygon(75, 200, 225, 200, 150, 100, fill="white", outline="black")
my_house.tag_bind(roof, '<Button-1>', clickRoof)
door = my_house.create_rectangle(130, 350, 170, 275, fill="white")
my_house.tag_bind(door, '<Button-1>', clickDoor)
handle = my_house.create_oval(135, 325, 140, 320, fill="white")
my_house.tag_bind(handle, '<Button-1>', clickHandle)
windowLeft = my_house.create_rectangle(100, 260, 130, 230, fill="white")
my_house.tag_bind(windowLeft, '<Button-1>', clickWindowLeft)
windowRight = my_house.create_rectangle(170, 260, 200, 230, fill="white")
my_house.tag_bind(windowRight, '<Button-1>', clickWindowRight)
sun = my_house.create_oval(30, 110, 110, 30, fill="white")
my_house.tag_bind(sun, '<Button-1>', clickSun)


# ELEPHANT DRAWING
#   -creates a picture of an elephant out of shapes using the create_oval, create_polygon and create_rectangle functions
#   -the elephant drawing's shapes are all initialized to white so the picture is not colorized
#   -each shape is bound to an action and function which changes the color of the shape if the user
#     clicked on the correct shape
#   -elephantOOPStext is initialized and will change depending on if the user clicks on the correct or wrong shapes
#   -elephanttext is initialized to ask user to find all the triangles in the elephant drawing
my_elephant= Canvas(elephant_frame, width=400, height=400, bg="cyan") # canvas for elephant drawing
my_elephant.pack(pady=20)
elephantOOPStext = my_elephant.create_text(200, 70, text=" ", font=('Ink Free', 20, 'bold'), justify = 'center', fill='black')
elephanttext = my_elephant.create_text(200, 40, text="Find TEN Circles!", font=('Kristen ITC', 20, 'bold'), justify = 'center', fill='black')
eleGrass = my_elephant.create_rectangle(3, 375, 400, 400, fill="white") # grass 
my_elephant.tag_bind(eleGrass, '<Button-1>', clickEleGrass)
leftleg = my_elephant.create_rectangle(200, 375, 250, 300, fill="white") # left leg
my_elephant.tag_bind(leftleg, '<Button-1>', clickLeftLeg)
rightleg = my_elephant.create_rectangle(300, 375, 350, 300, fill="white") # right leg
my_elephant.tag_bind(rightleg, '<Button-1>', clickRightLeg)
elephantbody = my_elephant.create_oval(175, 360, 380, 175, fill="white") # body
my_elephant.tag_bind(elephantbody, '<Button-1>', clickEleBody)
leftear = my_elephant.create_oval(40, 270, 135, 175, fill="white") # left ear
my_elephant.tag_bind(leftear, '<Button-1>', clickLeftEar)
inside_leftear = my_elephant.create_oval(50, 260, 125, 185, fill="white") # inside left ear
my_elephant.tag_bind(inside_leftear, '<Button-1>', clickInsideLeft)
rightear = my_elephant.create_oval(180, 270, 275, 175, fill="white") # right ear
my_elephant.tag_bind(rightear, '<Button-1>', clickRightEar)
inside_rightear = my_elephant.create_oval(190, 260, 265, 185, fill="white") # inside right ear
my_elephant.tag_bind(inside_rightear, '<Button-1>', clickInsideRight)
elephant_head = my_elephant.create_oval(110, 270, 205, 175, fill="white") # head
my_elephant.tag_bind(elephant_head, '<Button-1>', clickEleHead)
trunk = my_elephant.create_rectangle(147, 370, 167, 230, fill="white") # trunk
my_elephant.tag_bind(trunk, '<Button-1>', clickTrunk)
lefteye = my_elephant.create_oval(120, 230, 150, 200, fill="white")  # left eye
my_elephant.tag_bind(lefteye, '<Button-1>', clickLeftEye)
righteye = my_elephant.create_oval(165, 230, 195, 200, fill="white")  # right eye
my_elephant.tag_bind(righteye, '<Button-1>', clickRightEye)
rightpupil = my_elephant.create_oval(170, 230, 190, 210, fill="white")  # right pupil
my_elephant.tag_bind(rightpupil, '<Button-1>', clickRightPupil)
leftpupil = my_elephant.create_oval(125, 230, 145, 210, fill="white")  # left pupil
my_elephant.tag_bind(leftpupil, '<Button-1>', clickLeftPupil)


# TRAIN DRAWING
#   -creates a picture of an train out of shapes using the create_oval, create_polygon and create_rectangle functions
#   -the train drawing's shapes are all initialized to white so the picture is not colorized
#   -each shape is bound to an action and function which changes the color of the shape if the user
#     clicked on the correct shape
#   -trainOOPStext is initialized and will change depending on if the user clicks on the correct or wrong shapes
#   -traintext is initialized to ask user to find all the triangles in the train drawing
my_train = Canvas(train_frame, width=400, height=330, bg="midnight blue")
my_train.pack(pady=20)

trainOOPStext = my_train.create_text(200, 310, text=" ", font=('Ink Free', 20, 'bold'), justify = 'center', fill='white')
traintext = my_train.create_text(200, 20, text="Find the Triangle!", font=('Kristen ITC', 20, 'bold'), justify = 'center', fill='white')
vertBody = my_train.create_rectangle(50, 50, 175, 220, fill="white") #vertical body
my_train.tag_bind(vertBody, '<Button-1>', clickVertBody)
window = my_train.create_rectangle(75, 75, 150, 125, fill="white")  #window
my_train.tag_bind(window, '<Button-1>', clickWindow)
outwheel = my_train.create_oval(65, 200, 160, 290, fill="white")  #outer wheel
my_train.tag_bind(outwheel, '<Button-1>', clickOutWheel)
innerwheel = my_train.create_oval(85, 220, 140, 270, fill="white")  #inner wheel
my_train.tag_bind(innerwheel, '<Button-1>', clickInnerWheel)
horBody = my_train.create_rectangle(175, 135, 325, 220, fill="white")    #horizontal body
my_train.tag_bind(horBody, '<Button-1>', clickHorBody)
triangle = my_train.create_polygon(325, 135, 375, 220, 325, 220, fill="white",outline="black")    #triangle
my_train.tag_bind(triangle, '<Button-1>', clickTriangle)
middlewheel = my_train.create_oval(185, 221, 250, 290, fill="white")  #middle wheel
my_train.tag_bind(middlewheel, '<Button-1>', clickMiddleWheel)
frontwheel = my_train.create_oval(265, 221, 330, 290, fill="white")  #front wheel
my_train.tag_bind(frontwheel, '<Button-1>', clickFrontWheel)
wheelbar = my_train.create_rectangle(80, 250, 310, 260, fill="white")    #wheel bar
my_train.tag_bind(wheelbar, '<Button-1>', clickWheelBar)
chimneybase = my_train.create_rectangle(235, 75, 265, 135, fill="white")    #chimney base
my_train.tag_bind(chimneybase, '<Button-1>', clickChimneyBase)
chimney = my_train.create_rectangle(220, 50, 280, 75, fill="white")    #chimney top
my_train.tag_bind(chimney, '<Button-1>', clickChimney)

# sets the first screen (welcome screen) to the first screen to be shown
first_screen.pack(fill = 'both', expand = 1)


root.mainloop()
