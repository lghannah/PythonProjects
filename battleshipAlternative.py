# Liam Hannah
# Battleship
from graphics import *
from random import randrange

win = GraphWin("Battleship", 800, 800)

for row in (100, 200, 300, 400, 500, 600):
    for column in (100, 200, 300, 300, 400, 500, 600):
        board = Rectangle(Point(row, column), Point(row + 100, column + 100)).draw(win)
        board.setFill("blue")

win.getMouse()

grid = [["open", "open", "open", "open", "open", "open"],
        ["open", "open", "open", "open", "open", "open"],
        ["open", "open", "open", "open", "open", "open"],
        ["open", "open", "open", "open", "open", "open"],
        ["open", "open", "open", "open", "open", "open"],
        ["open", "open", "open", "open", "open", "open"]]

hit_counter = 0
click_counter = 0 
row = 10000
column = 10000

def main():
    global click_counter
    first = True
    winner = False
    while winner == False:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        if first:
            fiveship()
            fourship()
            threeship()
        if 100 <= x <= 700 and 100 <= y <= 700:
            click_counter += 1
            getColumn(y)
            getRow(x)
            display(row, column)
        if hit_counter == 12:
            winner = True
    winner_function()


    win.getMouse()


def fiveship():
    global grid, hit_counter, miss_counter
    orientation = randrange(1, 3)
    positionPrimary = randrange(0, 2)
    positionSecondary = randrange(0, 6)

    if orientation == 1:  # vertical
        grid[positionSecondary][positionPrimary] = "taken"
        grid[positionSecondary][positionPrimary + 1] = "taken"
        grid[positionSecondary][positionPrimary + 2] = "taken"
        grid[positionSecondary][positionPrimary + 3] = "taken"
        grid[positionSecondary][positionPrimary + 4] = "taken"

    else:
        grid[positionPrimary][positionSecondary] = "taken"
        grid[positionPrimary + 1][positionSecondary] = "taken"
        grid[positionPrimary + 2][positionSecondary] = "taken"
        grid[positionPrimary + 3][positionSecondary] = "taken"
        grid[positionPrimary + 4][positionSecondary] = "taken"


def fourship():
    global grid
    orientation = randrange(1, 3)
    positionPrimary = randrange(0, 3)
    positionSecondary = randrange(0, 6)

    #vertical
    if orientation == 1:
        while grid[positionSecondary][positionPrimary] == "taken" or grid[positionSecondary][positionPrimary + 1] == "taken" or \
        grid[positionSecondary][positionPrimary + 2] == "taken" or grid[positionSecondary][positionPrimary + 3] == "taken":
            positionPrimary = randrange(0, 3)
            positionSecondary = randrange(0, 6)

        grid[positionSecondary][positionPrimary] = "taken"
        grid[positionSecondary][positionPrimary + 1] = "taken"
        grid[positionSecondary][positionPrimary + 2] = "taken"
        grid[positionSecondary][positionPrimary + 3] = "taken"

    else:
        while grid[positionPrimary][positionSecondary] == "taken" or grid[positionPrimary + 1][positionSecondary] == "taken" or \
        grid[positionPrimary + 2][positionSecondary] == "taken" or grid[positionPrimary + 3][positionSecondary] == "taken":
           positionPrimary = randrange(0, 3)
           positionSecondary = randrange(0, 6)

        grid[positionPrimary][positionSecondary] = "taken"
        grid[positionPrimary + 1][positionSecondary] = "taken"
        grid[positionPrimary + 2][positionSecondary] = "taken"
        grid[positionPrimary + 3][positionSecondary] = "taken"

def threeship():
    global grid
    orientation = randrange(1, 3)
    positionPrimary = randrange(0, 3)
    positionSecondary = randrange(0, 6)

    # vertical
    if orientation == 1:
        while grid[positionSecondary][positionPrimary] == "taken" or grid[positionSecondary][positionPrimary + 1] == "taken" or \
        grid[positionSecondary][positionPrimary + 2] == "taken" or grid[positionSecondary][positionPrimary + 3] == "taken":
            positionPrimary = randrange(0, 3)
            positionSecondary = randrange(0, 6)

        grid[positionSecondary][positionPrimary] = "taken"
        grid[positionSecondary][positionPrimary + 1] = "taken"
        grid[positionSecondary][positionPrimary + 2] = "taken"

    else:
        while grid[positionPrimary][positionSecondary] == "taken" or grid[positionPrimary + 1][
            positionSecondary] == "taken" or \
                        grid[positionPrimary + 2][positionSecondary] == "taken" or grid[positionPrimary + 3][
            positionSecondary] == "taken":
            positionPrimary = randrange(0, 3)
            positionSecondary = randrange(0, 6)

        grid[positionPrimary][positionSecondary] = "taken"
        grid[positionPrimary + 1][positionSecondary] = "taken"
        grid[positionPrimary + 2][positionSecondary] = "taken"

def getColumn(y):
    global column
    
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

def getRow(x):      
    global row
    
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

def display(row, column):
    global grid, counter
    
    if grid[row - 1][column - 1] == "taken":
        rectangle = Rectangle(Point(row * 100, column * 100), Point(row * 100 + 100, column * 100 + 100))
        rectangle.setFill("red")
        rectangle.draw(win)
    elif grid[row - 1][column - 1] == "open":
        rectangle = Rectangle(Point(row * 100, column * 100), Point(row * 100 + 100, column * 100 + 100))
        rectangle.setFill("blue")
        rectangle.draw(win)
        

def winner_function():
    global click_counter
    
    number = str(click_counter)
    
    Text(Point(400, 725), "You win, " + number + " clicks!").draw(win)
    
    win.getMouse()
main()
