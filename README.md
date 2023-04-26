# CS2520-A6
Assignment 6 - Complete refactoring of graphics_v4.py

## Description

  Our objective is to modify the code in a way that allows for easy modifications such as altering object locations, quantities, and sizes. The main goal of this assignment is to enable the project to be quickly adapted to meet various requirements or design preferences.

  Using a previous coding project, we worked collaboratively to refactor the codebase. We thought carefully about how to structure the code to ensure it is modular and easy to maintain. Additionally, we ensured that the code adheres to best practices and coding conventions to ensure it is easily understandable by others.

  An important aspect of this assignment is the application of structural programming techniques. We edited the program in a functional form, focusing on organizing our code into clear, concise, and reusable functions that can be easily combined and modified as needed.

## Created Functions and Classes

def set_day() #changes scene to daytime colors

def set_night() #changes scene to nighttime colors

def draw_stars # x and y are the values in which the random range will produce the stars position

def draw_cloud(x, y) #draws the clouds in the desired coordinates

def generate_clouds(num_clouds) ## generate the number of desired clouds 

def check_events() #checks for inputs that would alter the game

class field #This is the field class, which draws the grass field and the stripes.
    
    def __init__()
    
    def draw()
    
class fence  #This is the fence class, which draws the fence
    
    def __init__()
    
    def draw()
    
def draw_lines() #draw_lines function is used to draw lines

def draw_safetyCircle() #Input the desired size the thickness of the safety circle

def draw_semicircle () #This function draws the arc at the top of the goal box

class scoreBoard #This is the scoreBoard Class, which is responsible for drawing the score board
    
    def __init__()
    
    def draw()

 class lightPole #This is the lightpole class, which is responsible for drawing the lightpoles
    
    def __init__()
    
    def draw()
    
def drawNet() #Draws net

def drawStands() #Draws stands

def drawFlags() #Draws flags
 
## Collaborators
Andrew Perez 
-lines 1 - 140

Jonathan Peña 
-lines 140 - 277

Aidan Zimmerman
-lines 279 - 382
