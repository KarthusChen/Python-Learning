## Larry Cortez
## CS 10 Intro to Programming Using Python
## Professor: Steven Allbee
## Assignment: tinkering around with Turtle & file processing

'''
Program Objective: Read a text file that contains AutoCAD line x,y coordinates
and draw the line entities in a Turtle graphic window
'''

#import turtle graphics for drawing, and csv for parsing input file
import turtle, csv

# Functioon to draw a line from (startpt_x, startpt_y, endpt_x, endpt_y)
def draw_line (tdrw, startpt_x, startpt_y, endpt_x, endpt_y):
    
    tdrw.penup()
    #start point of line segment
    tdrw.goto (startpt_x, startpt_y)
    tdrw.pendown()
    #end point of line segment
    tdrw.goto (endpt_x, endpt_y)
    tdrw.penup()
  
# Function to read a file
def read_file(filename):    
        
    #instantiate turtle object
    tdrw = turtle.Turtle()
    
    #set line color
    tdrw.color('forest green')
    
    #cursor movement range 0-10, 0=no animation motion, 10=fastest
    tdrw.speed(0)
    
    #prep to open a file for reading
    in_file = open(filename)
    
    #read_line input e.g. '11.0000,76.0000,19.0000,76.0000'
    read_line = in_file.readline()

    #loop thru each line in the file
    while read_line != "":
        
        #print(read_line, end="")
        
        coord_line = csv.reader([read_line])
        #create a list of x,y start and end points
        coord_list = list(coord_line)
        #coord_list e.g. [['11.0000','76.0000','19.0000','76.0000']]
        
        #x,y startpoint, convert string to float
        spx = float(coord_list[0][0])
        spy = float(coord_list[0][1])        
        #x,y endpoint, convert string to float
        epx = float(coord_list[0][2])
        epy = float(coord_list[0][3])    
        
        #function to draw a line
        draw_line(tdrw, spx, spy, epx, epy)
        #read next line
        read_line = in_file.readline()         
        
    #close file
    in_file.close()

#define the main function
def main():
    
    #var for file name to use for function write_file & read_file argument
    fname = "HouseFlrPlan.txt"      
    
    # set world coordinates
    turtle.setworldcoordinates(-1, -1, 540, 440)
    # Initailize screen size (width, height, startx, starty)
  
    #title the turtle window
    turtle.title ('CAD Viewer')    
    
    #function to read the text file containing the line coordinates
    read_file(fname)
        
    #The window will continue to be displayed until the user closes it
    turtle.done()
    
#execute the program
main()