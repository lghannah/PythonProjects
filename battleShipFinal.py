#battleship.py
#Liam Hannah
#Lab M5
#lghannah@syr.edu

#importing the libraries
from graphics import *
from random import randrange

#(CLOD)
#battleship class
class BattleShip:
    #creates the battleship object
    def __init__(self, length, pos):
        self.length = length
        self.pos = pos
    
#(CLOD)
#this class creates the player object and displays the name in the results file
class Player:
    #creates the player object
    def __init__(self, name):
        self.name = name

    #function that appends the player's name to a file
    def display(self):
        resultFile = open("results.txt", "a+")
        print("Name:",self.name, end= " Number of Clicks: ", file = resultFile)
    



################################################

#this function is the backbone of the game, it calls other functions and instantiates the battleship objects
#it checks for winners and draws onto the board
#the parameters are win, nameEntryBox, and grid which are there because it draws to the window, and checks the 2D array
#it includes nameEntryBox because other functions that it calls require the nameEntryBox    
def checkClick(win, nameEntryBox, grid):
    #instantiating that a win hasn't been made yet 
    winner = False
    #setting the amount of hits and clicks to 0 at the beginning
    hit_counter = 0
    click_counter = 0
    #list for the battleships
    shipList = []

    #(CLOD)
    #(LOOD)
    #creating the battleship objects and putting them in a list
    #ship that is five squares long
    fiveShip = BattleShip(5,2)
    shipList.append(fiveShip)

    #ship that is four squares long
    fourShip = BattleShip(4,3)
    shipList.append(fourShip)

    #ship that is three squares long
    threeShip = BattleShip(3,3)
    shipList.append(threeShip)

    #(FNC)
    #calling function that draws title and name label on the board
    board = displayInitial(win)

    #calling the function that places the ships by their length and max position from the end
    fiveShip = placeShip(5, 2, grid)
    fourShip = placeShip(4, 3, grid)
    threeShip = placeShip(3, 3, grid)

    #while loop for the game to go on while there isn't a winner
    while winner == False:
        #(IMS)
        #getting X and Y coords of click
        click = win.getMouse()
        x = click.getX()
        y = click.getY()

       #checking if the click is on the game board
        if 100 <= x <= 700 and 100 <= y <= 700:
            #click goes up by 1 each time
            click_counter += 1
            #(FNC)
            #calling the getColumn and getRow functions using x and y from the clicks
            getColumn(y)
            getRow(x)
            #if the display function returns true then that means its a hit
            if display(win, row, column, grid, hit_counter, click_counter) == True:
                #hit counter increates
                hit_counter += 1

        #if hit counter = 12 that means all the ships have been found and the game is over
        if hit_counter == 12:
            #winner is true now
            winner = True
            #(FNC)
            #calling the winner function
            winner_function(win, nameEntryBox, click_counter)
       
#this function places the ships on the board randomly and also has a check for overlapping ships
#the parameters are length, p, and grid
#length is the length of the ship which is important for placing the ship, p is the position that is the max spot they can be placed in before it goes off the game board
#grid is the 2D array which is used to check for taken spots and settign spots to taken when a ship is placed
def placeShip(length, p, grid):
    #opening the cheat sheet file that the ships location is printed to
    cheatSheet = open("cheatSheet.txt", "w")

    #instatiating overlap, orientation, positionPrimary, positionSecondary
    overlap = True
    orientation = 0
    positionPrimary = 0
    positionSecondary = 0

    #while loop for checking/preventing overlap
    while overlap:
        overlap = False
        #(RND)
        #random placecment of the ships
        orientation = randrange(1, 3)
        positionPrimary = randrange(1, p)
        positionSecondary = randrange(1, 6)

        #checking for overlap based on if the spot on the array is taken or not
        for i in range(0, length):
            if orientation == 1:
                if grid[positionSecondary][positionPrimary + i] == "taken":
                    overlap = True
            elif orientation == 2:
                if grid[positionPrimary + i][positionSecondary] == "taken":
                    overlap = True

    #setting the spot to taken if the orientation of the shit has it being placed there                
    if orientation == 1:
        for column in range(positionPrimary, positionPrimary + length):
            grid[positionSecondary][column] = "taken"
    else:
        for row in range(positionPrimary, positionPrimary + length):
            grid[row][positionSecondary] = "taken"

    #(OFL)
    #prints the location of the ships into the cheatsheet in lists column by column
    print(grid, file = cheatSheet)
     
#gets a column number based on the coordinates
#y is the parameter because it uses the y coord of where you click
def getColumn(y):
    global column

    #function for identifying column numbers based off y coord of click
    if 100 < y < 200:
        column = 1
    elif 200 < y < 300:
        column = 2
    elif 300 < y < 400:
        column = 3
    elif 400 < y < 500:
        column = 4
    elif 500 < y < 600:
        column = 5
    elif 600 < y < 700:
        column = 6

#returns the row number based on where you click
#x is the param because it uses x coords of where you click
def getRow(x):
    global row

    #function for identifying row numbers bsed on x coord of click
    if 100 < x < 200:
        row = 1
    elif 200 < x < 300:
        row = 2
    elif 300 < x < 400:
        row = 3
    elif 400 < x < 500:
        row = 4
    elif 500 < x < 600:
        row = 5
    elif 600 < x < 700:
        row = 6
        
#function just for displaying the the title and name label
#win is a parameter because it draws to the window
def displayInitial(win):
    #title of the game + font
    #(OTXT)
    title = Text(Point(390,50), "Battleship")
    title.setFace("courier")
    title.setSize(30)
    title.draw(win)

    #label for the text entry box
    nameLabel = Text(Point(540,50), "Name: ")
    nameLabel.draw(win)

#shows the squares once they've been clicked and whether its a hit or miss
#the parameteres are win, row, column, hit_counter and click_counter
#click counter goes up when theres a click on a square and hit counter goes up if its a hit
#row, column, and grid use coords and the 2D array, this is how this function will draw the rectangles and check if theres a ship in the spot
#win is because it draws the squares to the window
def display(win, row, column, grid, hit_counter, click_counter):
    #checking if the spot has been taken when clicked
    if grid[row - 1][column - 1] == "taken":
        #creates a red rectangle for a hit
        rectangle = Rectangle(Point(row * 100, column * 100), Point(row * 100 + 100, column * 100 + 100))
        rectangle.setFill("red")
        rectangle.draw(win)
        #hit and click_counter go up and return true
        hit_counter = hit_counter + 1
        click_counter = click_counter + 1
        return True
    #if the spot clicked is open
    elif grid[row - 1][column - 1] == "open":
        #creates a blue rectangle indicating a miss
        rectangle = Rectangle(Point(row * 100, column * 100), Point(row * 100 + 100, column * 100 + 100))
        rectangle.setFill("blue")
        rectangle.draw(win)
        #click_counter still goes up and returns false
        click_counter = click_counter + 1
        return False

#This function displays on the screen that you have won and then it calls the results function
#the parameters are win, nameEntryBox, and click_counter because it draws to the window and it takes info from the entry box to figure out the name
#it also draws to the window the amount of clicks you made 
def winner_function(win, nameEntryBox, click_counter):
    #making click_counter a string so that it can be concatonated
    number = str(click_counter)

    #(OTXT)
    #text that appears once you won showing the number of clicks you had
    winText = Text(Point(400, 725), "You win, " + number + " clicks!")
    winText.draw(win)

    #text that also is drawn once you win telling you to go check the results file
    resultText = Text(Point(400,740), "Check the text file results.txt to see how you and other players did!")
    resultText.draw(win)

    #getting the name from the entry box
    #(IEB)
    nameInput = nameEntryBox.getText()

    #(CLOD)
    #creating a player based on your name input in the entry box
    user = Player(nameInput)

    #calling results function
    #(FNC)
    result = results(win, user, click_counter)

#This function displays names and the amount of clicks it took to win in the result file
#the parameters are win, user, and click_counter because it takes info from the graph and prints the name of the player and their clicks to the file
def results(win, user, click_counter):
    #open infile/outfile and append name and score to it
    #(IFL)
    #(OFL)
    resultFile = open("results.txt", "a+")
    user.display()
    #printing the amount of clicks to the result file
    print(click_counter, file=resultFile)

#The main function creates the graph and instatiates variables that indicate its time to start the game
#It calls the check_click and winner functions which is how the game is played and ended
def main():
    #the graphics window
    #(GW)
    win = GraphWin("Battleship", 800, 800)

    #2D array for the grid
    #setting everything to open to indicate that ships haven't been placed yet
    grid = [["open", "open", "open", "open", "open", "open"],
            ["open", "open", "open", "open", "open", "open"],
            ["open", "open", "open", "open", "open", "open"],
            ["open", "open", "open", "open", "open", "open"],
            ["open", "open", "open", "open", "open", "open"],
            ["open", "open", "open", "open", "open", "open"]]

    #nested for loop to draw the gameboard
    for row in (100, 200, 300, 400, 500, 600):
        for column in (100, 200, 300, 300, 400, 500, 600):
            board = Rectangle(Point(row, column), Point(row + 100, column + 100))
            board.draw(win)

    #initializing row and column
    row = 0
    column = 0

    #booleans for the first turn and to say that no one has won yet
    first = True
    winner = False

    #creating the name entry box
    nameEntryBox = Entry(Point(610,50),10)
    nameEntryBox.draw(win)

    #the call to this function starts the game
    #(FNC)
    clickChecker = checkClick(win, nameEntryBox, grid)


    #closing the window after a click
    win.getMouse()
    win.close()
   
main()
